from django.contrib import admin
from .models import Supplier, InventoryItem, Purchase, InventoryTransaction

class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Add other fields if needed
    search_fields = ['name']  # Add fields you want to search by

admin.site.register(Supplier, SupplierAdmin)

class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'quantity', 'unit_price', 'supplier')
    search_fields = ['name', 'description', 'supplier__name']  # Add fields you want to search by
    list_filter = ['supplier']  # Add filters you want to apply

admin.site.register(InventoryItem, InventoryItemAdmin)

class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('item', 'quantity', 'total_price', 'purchase_date')
    search_fields = ['item__name']  # Add fields you want to search by
    list_filter = ['purchase_date']  # Add filters you want to apply

admin.site.register(Purchase, PurchaseAdmin)

class InventoryTransactionAdmin(admin.ModelAdmin):
    list_display = ('item', 'transaction_type', 'quantity', 'transaction_date')
    search_fields = ['item__name']  # Add fields you want to search by
    list_filter = ['transaction_type', 'transaction_date']  # Add filters you want to apply

admin.site.register(InventoryTransaction, InventoryTransactionAdmin)

