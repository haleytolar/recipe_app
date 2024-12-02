from django.contrib import admin
from django.urls import path, include  # Import 'include'

urlpatterns = [
    path('admin/', admin.site.urls),        # Admin routes
    path('', include('recipes.urls')),     # Connect to recipes app URLs
]

