from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.FloatField(default=0) 
    unit = models.CharField(max_length=200) 
    unit_price = models.FloatField(default=0) 

    def __str__(self):
        return f"{self.name} ({self.quantity} {self.unit} @ ${self.unit_price:.2f}/{self.unit})"

class MenuItem(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField(default=0)  # Selling price

    def __str__(self):
        return f"{self.title} - ${self.price:.2f}"

class RecipeRequirements(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)  # Quantity of ingredient needed for the recipe

    class Meta:
        verbose_name = "Recipe Requirement"
        verbose_name_plural = "Recipe Requirements"
        unique_together = ('menu_item', 'ingredient')  # Ensures no duplicate combinations

    def __str__(self):
        return f"{self.quantity} {self.ingredient.unit} of {self.ingredient.name} for {self.menu_item.title}"

class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)  # Automatically sets timestamp when created

    def __str__(self):
        return f"Purchased {self.menu_item.title} on {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"
