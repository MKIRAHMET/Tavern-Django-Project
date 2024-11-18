from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path('ingredients/', views.IngredientView.as_view(), name='ingredient_list'),
    path('ingredients/<pk>/update/', views.UpdateInventoryView.as_view(), name='update_inventory'),
    path("ingredients/add", views.AddIngredientInventoryView.as_view(), name='add_ingredient'),
    path("ingredients/<int:pk>/delete", views.DeleteIngredientInventoryView.as_view(), name='delete_ingredient'),
    path('menu/', views.MenuItemView.as_view(), name='menu_items'),
    path("menu/add_item", views.AddItemMenuView.as_view(), name='additem'),
    path("menu/<int:pk>/delete_item", views.DeleteItemMenuView.as_view(), name='deleteitem'),
    path('purchases/', views.PurchaseView.as_view(), name='purchases'),
    path("purchases/add", views.AddPurchaseView.as_view(), name = 'add_purchase'),
    path("purchases/<pk>/delete", views.DeletePurchaseView.as_view(), name="delete_purchase"),
    path('revenue/', views.RevenueView.as_view(), name='revenue'),
    path("recipe/add", views.AddRecipeRequirementsView.as_view(), name='add_requirements'),
    path("recipe/<pk>/delete", views.DeleteRecipeRequirementsView.as_view(), name = "delete_requirements"),
]
