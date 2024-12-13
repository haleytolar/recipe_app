from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    RecipeLoginView, RecipeLogoutView,
 search_recipes, home, recipe_list, recipe_detail, add_recipe, about_me
)


app_name = 'recipes'

urlpatterns = [
    path('', home, name='home'),
    path('recipes/', recipe_list, name='recipe_list'),
    path('recipes/<int:recipe_id>/', recipe_detail, name='recipe_detail'),
    path('login/', RecipeLoginView.as_view(), name='login'),
    path('logout/', RecipeLogoutView.as_view(), name='logout'),
    path('search/', search_recipes, name='search_recipes'),
    path('add-recipe/', add_recipe, name='add_recipe'),
    path('about-me/', about_me, name='about_me'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
