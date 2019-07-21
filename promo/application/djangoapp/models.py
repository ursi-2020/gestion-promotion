from django.db import models
from django.conf import settings
from django.utils import timezone

class Promotions(models.Model):
    isFlat = models.BooleanField()
    flat = models.FloatField()
    percent = models.FloatField()
    productId = models.PositiveIntegerField()

    def __str__(self):
        return 'Promotions product: {}'.format(self.productId)
