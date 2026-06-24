from django.db import models
from django.conf import settings

from addresses.models import Address
from products.models import Product

ORDER_STATUS = [('PENDING', 'Pending'),('CONFIRMED', 'Confirmed'),('SHIPPED', 'Shipped'),('DELIVERED', 'Delivered'),(
    'CANCELLED', 'Cancelled'),
]

class Order(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='orders'
    )

    address = models.ForeignKey(
        Address,
        on_delete=models.PROTECT
    )

    total_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    status = models.CharField(
        max_length=20,
        choices=ORDER_STATUS,
        default='PENDING'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return f"Order #{self.id}"
    

class OrderItem(models.Model):

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items'
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT
    )

    quantity = models.PositiveIntegerField()

    price = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    def __str__(self):

        return self.product.name