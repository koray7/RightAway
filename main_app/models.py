from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Grocery(models.Model):

    name = models.CharField(max_length=100)
    image = models.CharField(max_length=250)
    category = models.CharField(max_length=100)
    organic = models.BooleanField(default=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class GroceryList(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=250)
    groceries = models.ForeignKey(Grocery, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.groceries.name)

# 


