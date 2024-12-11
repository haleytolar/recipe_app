from django.test import TestCase
from django.urls import reverse
from recipes.models import Recipe


class RecipeModelTests(TestCase):
    def setUp(self):
        self.recipe = Recipe.objects.create(
            name="Avocado Toast",
            ingredients="1 ripe avocado\n2 slices of whole-grain bread\nSalt and pepper, to taste",
            instructions="Toast bread, mash avocado, season, and serve.",
            cooking_time=10,
            serving_size=1,
            image="recipes/avo_toast.jpeg",
            category="appetizer",
        )

    def test_recipe_creation(self):
        recipe = Recipe.objects.get(name="Avocado Toast")
        self.assertEqual(recipe.name, "Avocado Toast")
        self.assertEqual(recipe.category, "appetizer")
        self.assertEqual(recipe.cooking_time, 10)
        self.assertEqual(recipe.serving_size, 1)


class RecipeViewTests(TestCase):
    def setUp(self):
        self.recipe = Recipe.objects.create(
            name="Avocado Toast",
            ingredients="1 ripe avocado\n2 slices of whole-grain bread\nSalt and pepper, to taste",
            instructions="Toast bread, mash avocado, season, and serve.",
            cooking_time=10,
            serving_size=1,
            image="recipes/avo_toast.jpeg",
            category="appetizer",
        )

    def test_recipe_list_view(self):
        response = self.client.get(reverse('recipes:recipe_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Avocado Toast")
        self.assertTemplateUsed(response, 'recipes/recipe_list.html')

    def test_recipe_detail_view(self):
        response = self.client.get(reverse('recipes:recipe_detail', args=[self.recipe.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Avocado Toast")
        self.assertContains(response, "Toast bread, mash avocado, season, and serve.")
        self.assertTemplateUsed(response, 'recipes/recipe_detail.html')


class RecipeSearchTest(TestCase):
    def test_search_page_loads(self):
        response = self.client.get(reverse('recipes:search_recipes'))
        self.assertEqual(response.status_code, 200)


