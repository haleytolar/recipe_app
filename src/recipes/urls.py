from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    RecipeLoginView, RecipeLogoutView, protected_view,
    recipe_visualization, search_recipes, home, recipe_list, recipe_detail
)


app_name = 'recipes'

urlpatterns = [
    path('', home, name='home'),
    path('recipes/', recipe_list, name='recipe_list'),
    path('recipes/<int:recipe_id>/', recipe_detail, name='recipe_detail'),
    path('login/', RecipeLoginView.as_view(), name='login'),
    path('protected/', protected_view, name='protected'),
    path('logout/', RecipeLogoutView.as_view(), name='logout'),
    path('visualization/', recipe_visualization, name='recipe_visualization'),
    path('search/', search_recipes, name='search_recipes'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
