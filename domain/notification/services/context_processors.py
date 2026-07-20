def sidebar_counts(request):
    """
    Injected into every template via TEMPLATES.OPTIONS.context_processors.
    Keeps unread-notification badges etc. out of individual views.
    """
    if not request.user.is_authenticated:
        return {}

    from domain.notification.models import Notification

    return {
        "unread_notification_count": Notification.objects.filter(
            recipient=request.user, is_read=False
        ).count(),
    }
