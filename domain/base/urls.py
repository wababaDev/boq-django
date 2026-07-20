from django.urls import path

from domain.base.views import DashboardView
from domain.base.views.auth_views import BoqLoginView, BoqLogoutView

app_name = "base"

urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard"),
        path("login/", BoqLoginView.as_view(), name="login"),
    path("logout/", BoqLogoutView.as_view(), name="logout"),
]
