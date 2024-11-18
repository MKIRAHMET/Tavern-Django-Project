from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DeleteView, CreateView
from .models import Ingredient, MenuItem, Purchase
from .forms import MenuItemForm
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

  
# View ingredients in the inventory
class IngredientView(TemplateView):
    model = Ingredient
    template_name = 'ingredients.html'  # Replace with your actual template path
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ingredients'] = Ingredient.objects.all()
        return context

# Delete ingredients from the inventory
class DeleteIngredientView(DeleteView):
    model = Ingredient
    template_name = 'routes/delete_ingredient.html'
    success_url = reverse_lazy('ingredient_list')

class MenuItemView(ListView):
    model = MenuItem
    template_name = "menuitems.html"
    context_object_name = "menuitems"  # Custom name for context

    def get_queryset(self):
        print(MenuItem.objects.all())  # Debug to confirm data is being fetched
        return MenuItem.objects.all()
    
# View the purchases made at the restaurant
class PurchaseView(ListView):
    model = Purchase
    template_name = 'purchases.html'  # Replace with your actual template path
    context_object_name = 'purchases'  # Name to use for the object list in the template

# View the profit and revenue for the restaurant
class RevenueView(TemplateView):
    template_name = 'revenue.html'  # Replace with your actual template path

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Calculate revenue
        purchases = Purchase.objects.select_related('menu_item')
        revenue = sum(purchase.menu_item.price for purchase in purchases)

        # Calculate costs
        menu_items = MenuItem.objects.prefetch_related('reciperequirements_set__ingredient')
        costs = 0
        for item in menu_items:
            for requirement in item.reciperequirements_set.all():
                costs += requirement.quantity * requirement.ingredient.unit_price

        # Calculate profit
        profit = revenue - costs

        context['revenue'] = revenue
        context['profit'] = profit
        return context

