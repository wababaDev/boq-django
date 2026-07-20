from django.contrib import admin

from domain.base.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "role", "branch", "is_coo")
    list_filter = ("role", "is_coo")
    search_fields = ("user__username", "user__first_name", "user__last_name")
