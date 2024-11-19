from django.urls import path, include
from . import views


urlpatterns = [
    path("account/", include("django.contrib.auth.urls")),
    path("", views.index, name="index"),
    path('ingredients/', views.IngredientView.as_view(), name='ingredient_list'),
    path('ingredients/<pk>/update/', views.UpdateInventoryView.as_view(), name='update_inventory'),
    path("ingredients/add", views.AddIngredientInventoryView.as_view(), name='add_ingredient'),
    path("ingredients/<pk>/delete", views.DeleteIngredientView.as_view(), name='delete_ingredient'),
    path('menu/', views.MenuItemView.as_view(), name='menu_items'),
    path("menu/add_item", views.AddItemMenuView.as_view(), name='additem'),
    path("menu/<pk>/delete_item", views.DeleteItemMenuView.as_view(), name='deleteitem'),
    path("menu/<pk>/update", views.UpdateMenuRequirementsView.as_view(), name = "update_menuitem"),
    path('purchases/', views.PurchaseView.as_view(), name='purchases'),
    path("purchases/add", views.AddPurchaseView.as_view(), name = 'add_purchase'),
    path("purchases/<pk>/delete", views.DeletePurchaseView.as_view(), name="delete_purchase"),
    path("purchases/<pk>/update", views.UpdatePurchaseView.as_view(), name="update_purchase"),
    path('revenue/', views.RevenueView.as_view(), name='revenue'),
    path('recipe/', views.RecipeView.as_view(), name='recipe'),
    path("recipe/add", views.AddRecipeRequirementsView.as_view(), name='add_requirements'),
    path("recipe/<pk>/delete", views.DeleteRecipeRequirementsView.as_view(), name = "delete_requirements"),
    path("recipe/<pk>/update", views.UpdateRecipeRequirementsView.as_view(), name = "update_requirements"),
    path("signup/", views.SignUp.as_view(), name= "signup"),
    path("logout/", views.logout_request, name="logout"),
    

    

]
