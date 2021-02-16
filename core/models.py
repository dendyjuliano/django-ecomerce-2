from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.shortcuts import reverse

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    discount_price = models.IntegerField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)

    def get_price(self, *args, **kwargs):
        discount_price = self.discount_price
        price = self.price

        if(discount_price != None):
            discount = price * discount_price/100
            return price - discount
        else:
            return price

    def get_absolute_url(self):
        url = reverse("core:detail_product",kwargs={
            'slug':self.slug
        })
        return url

    def __str__(self):
        return self.title
