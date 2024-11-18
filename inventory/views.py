from django.urls import reverse_lazy
from django.views.generic import UpdateView, TemplateView, ListView, DeleteView, CreateView
from .models import Ingredient, MenuItem, Purchase, RecipeRequirements
from .forms import MenuItemForm, IngredientForm, RecipeRequirementsForm,UpdateInventoryForm
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

    #a page to add an item to the menu
class AddItemMenuView(CreateView):
    model = MenuItem
    form_class = MenuItemForm
    template_name = 'menucreate.html'
    
class DeleteItemMenuView(DeleteView):
    model = MenuItem
    success_url = 'menu/'
    template_name = 'delete_item.html'
    #a page to add an ingredient to the inventor
class AddIngredientInventoryView(CreateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = 'addingredient.html'
class DeleteIngredientInventoryView(DeleteView):
    model = Ingredient
    success_url = 'ingredients/'
    template_name = 'delete_ingredient.html'
    #a page to add the recipe requirements for a menu item
class AddRecipeRequirementsView(CreateView):
    model = RecipeRequirements
    form_class = RecipeRequirementsForm
    template_name = 'addrequirement.html'
class DeleteRecipeRequirementsView(DeleteView):
    model = RecipeRequirements
    success_url = 'ingredients/'
    template_name = 'delete_requirement.html'
    #a page to record a new purchase of a menu item
class AddPurchaseView(CreateView):
    model = MenuItem
    form_class = MenuItemForm
    template_name = 'menucreate.html'
class DeletePurchaseView(DeleteView):
    model = Purchase
    success_url = 'purchases/'
    template_name = 'delete_purchase.html'

   # a page to update the inventory for an existing ingredient
class UpdateInventoryView(UpdateView):
    model = Ingredient
    template_name = 'routes/update_inventory.html'
    form_class = UpdateInventoryForm

