from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=120)
    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
    

class Ingredient(models.Model):
    name = models.CharField(max_length=10)


    def __str__(self):
        return self.name
    

class Recipie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipies')
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="recipies")
    ingredients = models.ManyToManyField(Ingredient, related_name="recipies")

    def __str__(self):
        return self.name
    



