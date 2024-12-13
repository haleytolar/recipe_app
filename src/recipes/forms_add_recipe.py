from django import forms
from .models import Recipe

class AddRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'ingredients', 'instructions', 'cooking_time', 'serving_size', 'image', 'category']
        widgets = {
            'instructions': forms.Textarea(attrs={'rows': 5}),
        }
