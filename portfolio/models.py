from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)
    age = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=100)
    messages = models.CharField(max_length=100)
