from django.contrib import admin
from secondapp.models import PizzaShop, Pizza, Order


admin.site.register(PizzaShop)
admin.site.register(Pizza)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['pizza', 'name', 'phone', 'date']