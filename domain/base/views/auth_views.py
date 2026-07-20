from django.contrib.auth.views import LoginView, LogoutView


class BoqLoginView(LoginView):
    template_name = "auth/login.html"


class BoqLogoutView(LogoutView):
    next_page = "base:login"