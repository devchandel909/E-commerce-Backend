

from django.db import models
from django.conf import settings


class Address(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='addresses'
    )

    full_name = models.CharField(
        max_length=100
    )

    phone = models.CharField(
        max_length=15
    )

    address_line = models.TextField()

    city = models.CharField(
        max_length=100
    )

    state = models.CharField(
        max_length=100
    )

    postal_code = models.CharField(
        max_length=10
    )

    country = models.CharField(
        max_length=100,
        default='India'
    )

    is_default = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return (
            f"{self.full_name}"
            f" - "
            f"{self.city}"
        )
