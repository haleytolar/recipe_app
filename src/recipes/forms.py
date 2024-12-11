from django import forms
from recipes.models import Recipe

CHART_CHOICES = (
    ("bar", "Bar Chart"),
    ("pie", "Pie Chart"),
    ("line", "Line Chart"),
)

class RecipeSearchForm(forms.Form):
    name = forms.CharField(
        required=False, 
        label="Name", 
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Recipe Name"})
    )
    ingredients = forms.CharField(
        required=False, 
        label="Ingredients", 
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingredients (e.g., Garlic, Spaghetti)"})
    )
    max_cooking_time = forms.IntegerField(
        required=False,
        label="Max Cooking Time",
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Max Time in Minutes"})
    )
    serving_size = forms.IntegerField(
        required=False,
        label="Serving Size",
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Serving Size"})
    )
    category = forms.ChoiceField(
        required=False,
        choices=[("", "All"), ("main", "Main Course"), ("dessert", "Dessert"), ("appetizer", "Appetizer")],
        widget=forms.Select(attrs={"class": "form-control"}),
        label="Category"
    )
    chart_type = forms.ChoiceField(
        required=False,
        choices=CHART_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}),
        label="Chart Type"
    )
