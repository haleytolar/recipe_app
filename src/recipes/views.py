from django.shortcuts import render, get_object_or_404
from .models import Recipe
from django.views.generic import ListView

# Welcome page
def home(request):
    return render(request, 'recipes/recipes_home.html')

# Recipe list page
def recipe_list(request):
    recipes = Recipe.objects.all()  
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})

# Recipe details page
def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)  
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})
