# import time
# from django.core.mail import send_mail
# from shop.celery import app


# @app.tasks
# def celery_order_mail(email, body):
#     time.sleep(10)
#     full_link = f'Hi, thank you for order \n we will text you! \n {body}'
#     send_mail(
#         'From shop',
#         f'Thank you for ordering products from our shop!',
#         'jamalaskarovaa@gmail.com',
#         [email]
#     )