from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, Instance, created, **kwargs):
    """
    Update order total on lineitem update/create
    """
    Instance.order.update.total()


@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, Instance, **kwargs):
    """
    Update order total on lineitem delete
    """
    Instance.order.update.total()