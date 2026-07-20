from django.contrib import admin

from domain.notification.models import Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ("recipient", "message", "is_read", "created_at")
    list_filter = ("is_read",)
