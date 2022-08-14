import time
from django.core.mail import send_mail
from applications.spam.models import Contact
from shop.celery import app


@app.task
def spam_email():
    full_link = f'Hi! We are very happy that you are our customer!'
    for i in Contact.objects.all():
        send_mail(
            'From shop project',
            full_link,
            'jamalaskarovaa@gmail.com',
            [i.email]
        )
