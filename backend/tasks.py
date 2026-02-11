from celery import shared_task
from .utils import import_shop
from django.core.mail import send_mail

@shared_task
def do_import(url):
    import_shop(url)

@shared_task
def send_email_task(subject, message, to):
    send_mail(subject, message, None, [to])
