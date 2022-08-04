import email
import time
from django.core.mail import send_mail
from applications.spam.models import Contact
from shop.celery import app


@app.task
def spam_email_for_product():
    for i in Contact.objects.all():
        time.sleep(10)
        full_link = f'Hi! We have new product!'
        send_mail(
            'From shop project',
            full_link,
            'jamalaskarovaa@gmail.com',
            [email]
        )
