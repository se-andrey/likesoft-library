from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_welcome_email(user_email):
    subject = 'Добро пожаловать в Библиотеку'
    message = 'Спасибо за регистрацию в нешуй электронно Библиотеке'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user_email]
    send_mail(subject, message, from_email, recipient_list)
