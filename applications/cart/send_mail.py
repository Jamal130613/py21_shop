from django.core.mail import send_mail


def order_mail(email, body):
    full_link = f'Hi, thank you for order \n we will text you! \n {body}'
    send_mail(
        'From shop',
        f'Thank you for ordering products from our shop!',
        'jamalaskarovaa@gmail.com',
        [email]
    )