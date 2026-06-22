from django.db import models
from django.conf import settings

from products.models import Product


class Wishlist(models.Model):

    # Wishlist owner

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='wishlist_items'
    )

    # Product saved

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='wishlisted_by'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        # Same user same product ko sirf ek baar add kar sakta hai

        unique_together = (
            'user',
            'product'
        )

    def __str__(self):

        return f"{self.user.username} - {self.product.name}"