from django.test import TestCase
from .models import Recipe

class RecipeModelTest(TestCase):

    def test_string_representation(self):
        recipe = Recipe(name="Test Recipe")
        self.assertEqual(str(recipe), recipe.name)