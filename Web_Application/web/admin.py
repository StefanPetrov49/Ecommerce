from django.contrib import admin

from Web_Application.web.models import Customer, Product, Order, OrderItem, ShippingAddress

# Register your models here.


admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'email']
    list_filter = ['user', 'name', 'email']


admin.site.register(Customer, CustomerAdmin)