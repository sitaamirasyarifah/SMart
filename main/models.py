from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    
