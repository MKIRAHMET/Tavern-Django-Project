from django.urls import path
from . import views


urlpatterns = [
    path('ingredients/', views.IngredientView.as_view(), name='ingredient_list'),
    path('ingredients/<pk>/delete/', views.DeleteIngredientView.as_view(), name='delete_ingredient'),
    path('menu/', views.MenuItemView.as_view(), name='menu_items'),
    path('purchases/', views.PurchaseView.as_view(), name='purchases'),
    path('revenue/', views.RevenueView.as_view(), name='revenue'),
    path("", views.index, name="index"),
]
