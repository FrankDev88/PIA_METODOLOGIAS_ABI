
# food/admin.py
from django.contrib import admin
from .models import FoodCategory, FoodItem

class FoodItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'available', 'created_at')  # Campos a mostrar
    list_filter = ('category', 'available')  # Filtros
    search_fields = ('name', 'category__name')  # Búsqueda por nombre y categoría
    ordering = ('created_at',)  # Ordenar por fecha de creación

class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Campos a mostrar
    search_fields = ('name',)  # Búsqueda por nombre
    ordering = ('name',)  # Ordenar por nombre

admin.site.register(FoodCategory, FoodCategoryAdmin)
admin.site.register(FoodItem, FoodItemAdmin)
