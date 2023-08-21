from django.contrib import admin
from .models import Checkout

class CheckoutAdmin(admin.ModelAdmin):
    list_display = ('name','email','address','invoice_no','total_bill')

# Register your models here.
admin.site.register(Checkout,CheckoutAdmin)