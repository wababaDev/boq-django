from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", include("domain.base.urls", namespace="base")),
    path("notifications/", include("domain.notification.urls", namespace="notification")),
    path("boq/", include("domain.boq.urls", namespace="boq")),
    path("catalog/", include("domain.catalog.urls", namespace="catalog")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
