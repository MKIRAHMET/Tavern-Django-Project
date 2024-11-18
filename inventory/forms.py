from .models import MenuItem
from django import forms

class MenuItemForm(forms.ModelForm):
  class Meta:
    model = MenuItem
    fields = "__all__"
