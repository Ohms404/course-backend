from django.db import models
# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=255, unique=True)
    second_name = models.CharField(max_length=255, unique=True)
    telephone = models.BigIntegerField(max_length=12, unique=True, null=False)

    def __str__(self):
        return self.first_name
