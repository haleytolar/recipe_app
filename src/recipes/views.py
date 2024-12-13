from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from io import BytesIO
import matplotlib.pyplot as plt
import pandas as pd
import base64
from .models import Recipe
from .forms import RecipeSearchForm
from .forms_add_recipe import AddRecipeForm
from django.contrib import messages


def home(request):
    search_form = RecipeSearchForm()
    return render(request, 'home.html', {'search_form': search_form})


def recipe_list(request):
    form = RecipeSearchForm(request.GET or None)
    recipes = Recipe.objects.all()
    chart = None

    if form.is_valid():
        name = form.cleaned_data.get("name")
        ingredients = form.cleaned_data.get("ingredient")
        max_cooking_time = form.cleaned_data.get("max_cooking_time")
        chart_type = form.cleaned_data.get("chart_type")

        if name:
            recipes = recipes.filter(name__icontains=name)
        if ingredients:
            recipes = recipes.filter(ingredients__in=ingredients).distinct()
        if max_cooking_time:
            recipes = recipes.filter(cooking_time__lte=max_cooking_time)

        if chart_type and recipes.exists():
            df = pd.DataFrame.from_records(recipes.values("name", "cooking_time"))
            chart = get_chart(chart_type, df)

    return render(request, "recipes/recipe_list.html", {"form": form, "recipes": recipes, "chart": chart})


def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})
class RecipeLoginView(LoginView):
  
    template_name = 'login.html'

class RecipeLogoutView(LogoutView):
    
    template_name = 'success.html'


def search_recipes(request):
   
    form = RecipeSearchForm(request.GET or None)
    recipes = Recipe.objects.all()  
    chart = None  


    if request.GET and form.is_valid():
        name = form.cleaned_data.get("name")
        ingredients = form.cleaned_data.get("ingredients")
        max_cooking_time = form.cleaned_data.get("max_cooking_time")
        serving_size = form.cleaned_data.get("serving_size")
        category = form.cleaned_data.get("category")
        chart_type = form.cleaned_data.get("chart_type")


        if name:
            recipes = recipes.filter(name__icontains=name)
        if ingredients:
            recipes = recipes.filter(ingredients__icontains=ingredients).distinct()
        if max_cooking_time:
            recipes = recipes.filter(cooking_time__lte=max_cooking_time)
        if serving_size:
            recipes = recipes.filter(serving_size=serving_size)
        if category:
            recipes = recipes.filter(category=category)


        if chart_type and recipes.exists():
            df = pd.DataFrame.from_records(recipes.values("name", "cooking_time"))
            chart = get_chart(chart_type, df)

    
    return render(request, 'recipes/search_results.html', {
        'form': form,
        'recipes': recipes,
        'chart': chart
    })


def get_chart(chart_type, data):
    if data.empty:
        return None

    plt.switch_backend("AGG")
    fig = plt.figure(figsize=(10, 6))

    if chart_type == "bar":
        plt.bar(data["name"], data["cooking_time"], color="skyblue")
        plt.title("Bar Chart: Cooking Time by Recipe")
        plt.ylabel("Cooking Time (min)")
        plt.xticks(rotation=45, ha='right')  

    elif chart_type == "pie":
        plt.pie(data["cooking_time"], labels=data["name"], autopct="%1.1f%%", startangle=140)
        plt.title("Pie Chart: Cooking Time Distribution")

    elif chart_type == "line":
        plt.plot(data["name"], data["cooking_time"], marker="o")
        plt.title("Line Chart: Cooking Time by Recipe")
        plt.ylabel("Cooking Time (min)")
        plt.xticks(rotation=45, ha='right')  

    buffer = BytesIO()
    plt.tight_layout()  
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    image_data = base64.b64encode(buffer.read()).decode("utf-8")
    buffer.close()

    return image_data



@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = AddRecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Recipe added successfully!')
            return redirect('recipes:recipe_list') 
    else:
        form = AddRecipeForm()
    return render(request, 'recipes/add_recipe.html', {'form': form})


def about_me(request):
    return render(request, 'recipes/about_me.html')