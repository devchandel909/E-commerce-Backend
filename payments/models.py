from django.db import models
from django.conf import settings

from orders.models import Order


class Payment(models.Model):

    PAYMENT_STATUS = [

        ('PENDING', 'Pending'),

        ('SUCCESS', 'Success'),

        ('FAILED', 'Failed'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='payments'
    )

    order = models.OneToOneField(
        Order,
        on_delete=models.CASCADE,
        related_name='payment'
    )

    razorpay_order_id = models.CharField(
        max_length=255,
        blank=True
    )

    razorpay_payment_id = models.CharField(
        max_length=255,
        blank=True
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS,
        default='PENDING'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return (
            f"Payment {self.id}"
        )
