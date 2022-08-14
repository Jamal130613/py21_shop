import email
import time
from django.core.mail import send_mail
from applications.spam.models import Contact
from shop.celery import app
from django.template.loader import render_to_string


@app.task
def send_product_info(name):
    # text = f'Hi! We have new product on our site {name}! http:/localhost:8000/ '
    html_message2 = render_to_string('send_mail.html', {'name': name})

    for user in Contact.objects.all():
        send_mail(
            'From shop project',
            '',
            'jamalaskarovaa@gmail.com',
            [user.email],
            html_message=html_message2,
        )
