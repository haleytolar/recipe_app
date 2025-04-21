from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from .models import Recipe


class RecipeViewTests(TestCase):
    def setUp(self):
        # creating a mock image file for the recipe
        image_file = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
        
        # creating the recipe objects
        self.recipe1 = Recipe.objects.create(name="Pasta", image=image_file)
        self.recipe2 = Recipe.objects.create(name="Salad", image=image_file)

    def test_recipe_list_view(self):
        # ensure the view renders correctly
        response = self.client.get(reverse('recipe_list'))  # Assuming 'recipe_list' is the name of the URL
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Pasta")
        self.assertContains(response, "Salad")

    def test_recipe_update_view(self):
        # test updating a recipe
        self.recipe1.name = 'Updated Pasta'
        self.recipe1.save()
        self.recipe1.refresh_from_db()  # Reload the object from the database
        self.assertEqual(self.recipe1.name, 'Updated Pasta')

    def test_search_recipes_view(self):
        # ensure search view works correctly
        response = self.client.get(reverse('search_recipes'))  # Assuming 'search_recipes' is the name of the URL
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Pasta")
        self.assertContains(response, "Salad")

    def test_recipe_list_view_no_image(self):
        # testing without uploading an image
        recipe_no_image = Recipe.objects.create(name="No Image Pasta")
        response = self.client.get(reverse('recipe_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No Image Pasta")

    def test_recipe_update_view_without_image(self):
        # test updating a recipe without an image
        recipe_no_image = Recipe.objects.create(name="Pasta Without Image")
        recipe_no_image.name = "Updated Pasta Without Image"
        recipe_no_image.save()
        recipe_no_image.refresh_from_db()
        self.assertEqual(recipe_no_image.name, "Updated Pasta Without Image")

    def tearDown(self):
        # clean up after tests if needed
        self.recipe1.delete()
        self.recipe2.delete()

