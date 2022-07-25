from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

User = get_user_model()


class Category(models.Model):
    title = models.TextField(max_length=100)
    slug = models.SlugField(primary_key=True,
                            max_length=100,
                            unique=True,
                            blank=True)
    parent = models.ForeignKey('self',
                               on_delete=models.CASCADE,
                               null=True,
                               blank=True,
                               related_name='children')

    def save(self, *args, **kwargs):
        self.slug = self.title.lower()
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        if self.parent:
            return f'{self.parent} -> {self.slug}'
        else:
            return self.slug


class Product(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name='products',
                              )
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.PositiveIntegerField(default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    # image = models.ImageField(upload_to='products')

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(upload_to='products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='images')


class Like(models.Model):
    """
    Модель лайков
    """
    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name='likes',
                              verbose_name='Like owner',)
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='likes',
                                verbose_name='Product')
    like = models.BooleanField('like', default=False)

    def __str__(self):
        return f'{self.product}  {self.like}'


class Rating(models.Model):
    """
    Модель рейтингов
    """
    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name='ratings',
                              verbose_name='Rating owner')
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='ratings',
                                verbose_name='Product')
    rating = models.SmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ], default=1
    )

    def __str__(self):
        return f'{self.product} - {self.rating}'


class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product}'

