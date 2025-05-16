
# Create your models here.
from django.db import models

class FoodCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='food_images/', blank=True, null=True)
    category = models.ForeignKey(FoodCategory, on_delete=models.SET_NULL, null=True, related_name='food_items')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
