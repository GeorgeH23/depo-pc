from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name
    

class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True,
                                on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    in_stock = models.BooleanField(default=False, null=True, blank=True)
    image = models.URLField(max_length=1024, null=True, blank=True)
    stars = models.DecimalField(max_digits=6, decimal_places=2, null=True,
                                blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    isBestSeller = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    products = models.ManyToManyField(Product)

    class Meta:
        verbose_name_plural = 'favorites'

    def __str__(self):
        return f'Favorites for {self.user.username}'
