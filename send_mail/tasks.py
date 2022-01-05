from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_mail_to_email(name, email, message, position):
    send_mail(subject=name,
              message=f'{message}\n\n{position}',
              recipient_list=[email, ],
              from_email=None)
