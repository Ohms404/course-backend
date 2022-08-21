from django.db import models
from product.models import Product
from user.models import User


# Create your models here.

class Cart(models.Model):
    product = models.ManyToManyField(Product)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
