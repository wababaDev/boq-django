"""
Business logic for creating/sending notifications -- both in-app and
email. Views call into this rather than touching Notification.objects
directly, so the async/email bits are swappable in one place.
"""
from domain.notification.models import Notification
from domain.notification.tasks import send_notification_email


def notify_user(user, message: str, link: str = "", email: bool = False):
    notification = Notification.objects.create(recipient=user, message=message, link=link)
    if email and user.email:
        send_notification_email.delay(user.id, message, link)
    return notification
