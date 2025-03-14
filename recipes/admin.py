from django.contrib import admin
from .models import Category, Recipe

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  ...
  
@admin.register(Recipe)
class RecipesAdmin(admin.ModelAdmin):
  ...
  
# admin.site.register(Category, CategoryAdmin)

