from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import InventoryTransaction, InventoryItem

@receiver(post_save, sender=InventoryTransaction)
def update_inventory_item_quantity(sender, instance, created, **kwargs):
    # Ensure the transaction is created and not being deleted
    if created and not kwargs.get('deleted', False):
        if instance.transaction_type == 'IN':
            # Increase the quantity when the transaction type is 'IN'
            instance.item.quantity += instance.quantity
        elif instance.transaction_type == 'OUT':
            # Decrease the quantity when the transaction type is 'OUT'
            instance.item.quantity -= instance.quantity
        # Save the InventoryItem instance to persist the changes
        instance.item.save()
