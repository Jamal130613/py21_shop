from django.core.mail import send_mail


def send_confirmation_email(code, email):
    full_link = f'http://localhost:8000/api/v1/account/active/{code}'
    send_mail(
        'From shop project',
        full_link,
        'jamalaskarovaa@gmail.com',
        [email]
    )