from django.urls import reverse_lazy
from django.views.generic import UpdateView, TemplateView, ListView, DeleteView, CreateView
from .models import Ingredient, MenuItem, Purchase, RecipeRequirements
from .forms import MenuItemForm, PurchaseForm, IngredientForm, RecipeRequirementsForm,UpdateInventoryForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout

def index(request):
    return render(request, 'index.html')

class SignUp(CreateView):
  form_class = UserCreationForm
  success_url = reverse_lazy("login")
  template_name = "registration/signup.html"


def logout_request(request):
  logout(request)
  return redirect("index")
    
# View ingredients in the inventory
class IngredientView(LoginRequiredMixin, TemplateView):
    model = Ingredient
    template_name = 'ingredients.html'  # Replace with your actual template path
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ingredients'] = Ingredient.objects.all()
        return context

# Delete ingredients from the inventory
class DeleteIngredientView(LoginRequiredMixin, DeleteView):
    model = Ingredient
    template_name = 'delete_ingredient.html'
    success_url = reverse_lazy('ingredient_list')

class MenuItemView(LoginRequiredMixin, ListView):
    model = MenuItem
    template_name = "menuitems.html"
    context_object_name = "menuitems"  

class RecipeView(LoginRequiredMixin, ListView):
    model = RecipeRequirements
    template_name = "recipe.html"
    context_object_name = "recipe"  

    def get_queryset(self):
        print(MenuItem.objects.all())  
        return MenuItem.objects.all()
    
# View the purchases made at the restaurant
class PurchaseView(LoginRequiredMixin, ListView):
    model = Purchase
    template_name = 'purchases.html'  
    context_object_name = 'purchases'  

# View the profit and revenue for the restaurant
class RevenueView(LoginRequiredMixin, TemplateView):
    template_name = 'revenue.html'  

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

class AddItemMenuView(LoginRequiredMixin, CreateView):
    model = MenuItem
    form_class = MenuItemForm
    template_name = 'menucreate.html'
    

class UpdateMenuRequirementsView(LoginRequiredMixin, UpdateView):
    model = MenuItem
    form_class = MenuItemForm
    template_name = 'updateitem.html'
    
class DeleteItemMenuView(LoginRequiredMixin, DeleteView):
    model = MenuItem
    success_url = reverse_lazy('menu_items')
    template_name = 'delete_item.html'

class AddIngredientInventoryView(LoginRequiredMixin, CreateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = 'addingredient.html'

class AddRecipeRequirementsView(LoginRequiredMixin, CreateView):
    model = RecipeRequirements
    form_class = RecipeRequirementsForm
    template_name = 'addrequirement.html'
    
class DeleteRecipeRequirementsView(LoginRequiredMixin, DeleteView):
    model = RecipeRequirements
    success_url = reverse_lazy('recipe')
    template_name = 'delete_requirement.html'

class AddPurchaseView(LoginRequiredMixin, CreateView):
    model = Purchase
    form_class = PurchaseForm
    template_name = 'purchasecreate.html'
    
class DeletePurchaseView(LoginRequiredMixin, DeleteView):
    model = Purchase
    success_url = ''
    template_name = 'delete_purchase.html'
    
class UpdatePurchaseView(LoginRequiredMixin, UpdateView):
    model = MenuItem
    template_name = "updateitem.html"
    form_class = MenuItemForm

class UpdateInventoryView(LoginRequiredMixin, UpdateView):
    model = Ingredient
    template_name = 'update_inventory.html'
    form_class = UpdateInventoryForm

class UpdateRecipeRequirementsView(LoginRequiredMixin, UpdateView):
    model = RecipeRequirements
    form_class = RecipeRequirementsForm
    template_name = 'updaterequirements.html'
    
