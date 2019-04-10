import uuid

from django.db import models


class Receipt(models.Model):
    receipt_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    store = models.CharField(max_length=64)
    purchase_date = models.DateField()
    date_updated = models.DateField()
    total_price = models.FloatField()
    tax = models.FloatField()
    picture = models.ImageField(blank=True)

    def __str__(self):
        return self.receipt_id

    # def delete(self):
    #     self.delete()