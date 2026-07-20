from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied


class RoleRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    """
    Subclass and set `allowed_roles = [Profile.Role.HOD, ...]`.
    Falls back to a 403 rather than a redirect once the user is known
    to be authenticated but simply not permitted.
    """

    allowed_roles: list[str] = []
    raise_exception = True

    def test_func(self):
        profile = getattr(self.request.user, "profile", None)
        if profile is None:
            return False
        return profile.role in self.allowed_roles

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            raise PermissionDenied("You don't have permission to access this page.")
        return super().handle_no_permission()


class BlocManagerRequiredMixin(RoleRequiredMixin):
    allowed_roles = ["bloc_manager"]


class COORequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        profile = getattr(self.request.user, "profile", None)
        return bool(profile and profile.is_coo)
