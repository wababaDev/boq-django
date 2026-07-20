from celery import shared_task
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_notification_email(user_id: int, message: str, link: str = ""):
    User = get_user_model()
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return
    send_mail(
        subject="GS Business Finance Loan System — Notification",
        message=f"{message}\n\n{link}",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user.email],
    )
