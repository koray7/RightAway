from django.contrib import admin
from .models import Grocery, GroceryList
# Register your models here.

admin.site.register(Grocery)
admin.site.register(GroceryList)