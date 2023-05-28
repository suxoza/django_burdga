from django.db import models
from django.utils.timezone import now


class Post(models.Model):
    title = models.CharField(max_length=100, default="")
    price = models.DecimalField(
        max_digits=4, max_length=4, default=0.00, decimal_places=4
    )

    description = models.CharField(max_length=100, default="")

    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(null=True, blank=True)
