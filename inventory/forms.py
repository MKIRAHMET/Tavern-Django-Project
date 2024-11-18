from .models import Ingredient, MenuItem, Purchase, RecipeRequirements
from django import forms

class MenuItemForm(forms.ModelForm):
  class Meta:
    model = MenuItem
    fields = "__all__"

class IngredientForm(forms.ModelForm):
  class Meta:
    model = Ingredient
    fields = "__all__"
    
class RecipeRequirementsForm(forms.ModelForm):
  class Meta:
    model = RecipeRequirements
    fields = "__all__"

class UpdateInventoryForm(forms.ModelForm):
  class Meta:
    model = Ingredient
    fields = "__all__"
