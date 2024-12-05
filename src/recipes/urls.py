from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


app_name = 'recipes'

urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/', views.recipe_list, name='recipe_list'),
    path('recipes/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)