from django.contrib import admin
from .models import Service, Invoice, Payment

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')  # Add other fields if needed
    search_fields = ['name']  # Add fields you want to search by

admin.site.register(Service, ServiceAdmin)

class InvoiceInline(admin.TabularInline):
    model = Invoice.services.through
    extra = 1

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('patient', 'date_created', 'total_amount', 'is_paid')
    search_fields = ['patient__name']  # Add fields you want to search by
    inlines = [InvoiceInline]

admin.site.register(Invoice, InvoiceAdmin)

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('invoice', 'amount', 'date_paid')
    search_fields = ['invoice__patient__name']  # Add fields you want to search by

admin.site.register(Payment, PaymentAdmin)


