from django.conf import settings
from django.shortcuts import render, get_object_or_404
from .models import Recipe
from django.views.generic import ListView
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView

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

class RecipeLoginView(LoginView):
    template_name = 'login.html'

class RecipeLogoutView(LogoutView):
    template_name = 'success.html'

@login_required
def protected_view(request):
    return render(request, 'protected.html')

def protected_view(request):
    print(settings.TEMPLATES[0]['DIRS'])
    return render(request, 'protected.html')