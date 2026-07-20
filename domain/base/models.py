from django.conf import settings
from django.db import models


class Profile(models.Model):
    """
    Extends the built-in User with app-specific role/branch info.
    Swap this for a custom AUTH_USER_MODEL later if needed -- for now
    a OneToOne keeps migrations simple while the domain apps are
    still being figured out.
    """

    class Role(models.TextChoices):
        STAFF = "staff", "Staff"
        BRANCH_MANAGER = "branch_manager", "Branch Manager"
        BLOC_MANAGER = "bloc_manager", "Bloc Manager"
        HOD = "hod", "Head of Department"
        COO = "coo", "COO"
        FINANCE = "finance", "Finance"
        ADMIN = "admin", "System Admin"

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile"
    )
    role = models.CharField(max_length=32, choices=Role.choices, default=Role.STAFF)
    branch = models.CharField(max_length=100, blank=True)
    is_coo = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.get_full_name() or self.user.username} ({self.get_role_display()})"
