from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    cooking_time = models.IntegerField(help_text="Time in minutes")
    ingredients = models.TextField(help_text="Comma-separated list of ingredients")

    def __str__(self):
        return self.name