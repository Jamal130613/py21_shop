from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver

from applications.product.models import Product

User = get_user_model()


class Order(models.Model):
    CART_STATUS = (
        ('in_processing', 'in_processing'),
        ('completed', 'completed'),
        ('declined', 'declined')
    )
    # product = models.ForeignKey(Product,
    #                             on_delete=models.CASCADE,
    # related_name='orders')
    customer = models.ForeignKey(User,
                                 on_delete=models.CASCADE,
                                 related_name='orders')
    total_cost = models.DecimalField(max_digits=100,
                                     decimal_places=2,
                                     default=0)
    # quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=CART_STATUS, default='in_processing')
    address = models.TextField()
    number = models.TextField()
    first_name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    info = models.TextField(blank=True)

    def __str__(self):
        return f'{self.first_name} ordered'

    # def save(self, *args, **kwargs):
    #     self.total_cost = self.product.price * self.quantity
    #     super().save(*args, **kwargs)


class Cart(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='carts',
                             )
    total_cost = models.DecimalField(max_digits=100,
                                     decimal_places=2,
                                     default=0)

    def __str__(self):
        return self.user.email


class CartItem(models.Model):
    cart = models.ForeignKey(Cart,
                             on_delete=models.CASCADE,
                             related_name='cart_items')
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='cart_items')
    quantity = models.PositiveIntegerField()
    total_cost = models.DecimalField(max_digits=100,
                                     decimal_places=2,
                                     default=0)

    def __str__(self):
        return f'{self.cart.id} {self.product}'

    def save(self, *args, **kwargs):
        self.total_cost = self.product.price * self.quantity

        try:
            cartitem = CartItem.objects.get(id=self.id)
            cartitem.cart.total_cost = cartitem.cart.total_cost - \
                                       cartitem.total_cost + \
                                       self.total_cost
            cartitem.cart.save()
        except CartItem.DoesNotExist:
            self.cart.total_cost += self.total_cost
            self.cart.save()

        super(CartItem, self).save()


@receiver(post_delete, sender=CartItem)
def delete_signal(sender, instance, **kwargs):
    instance.cart.total_cost -= instance.total_cost
    instance.cart.save()


