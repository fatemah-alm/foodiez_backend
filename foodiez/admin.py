from django.contrib import admin
from .models import Category, Recipie, Ingredient
# Register your models here.

admin.site.register(Category)
admin.site.register(Recipie)
admin.site.register(Ingredient)