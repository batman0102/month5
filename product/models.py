from django.db import models
from django.db.models import Avg


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def products_count(self):
        return self.products.count()

class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='products'
    )

    def __str__(self):
        return self.title

    def category_name(self):
        return self.category.name

    def average_rating(self):
        return self.reviews.aggregate(Avg('stars'))['stars__avg'] or 0.0

class Review(models.Model):

    STARS = (
        (1, '*'),
        (2, '**'),
        (3, '***'),
        (4, '****'),
        (5, '*****')
    )

    text = models.TextField(max_length=200)
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        related_name='reviews'
    )
    stars = models.IntegerField(choices=STARS, default=3)

    def __str__(self):
        return self.text


