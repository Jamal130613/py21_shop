from django.db import models


class Contact(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


# TODO: реализовать отправку спам сообщений всем объектам из модели Contact;
#       При создании товара отправлять сообщение всем объектам из модели Contact.
