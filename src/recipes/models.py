from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField()
    instructions = models.TextField()
    cooking_time = models.PositiveIntegerField()
    serving_size = models.PositiveIntegerField()
    image = models.ImageField(upload_to='recipes/')
    category = models.CharField(
        max_length=50,
        choices=[
            ('main', 'Main Course'),
            ('dessert', 'Dessert'),
            ('appetizer', 'Appetizer'),
        ],
    )

