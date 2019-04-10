from django.db import models


class Receipt(models.Model):
    receipt_id = models.UUIDField()
    store = models.CharField(max_length=64)
    purchase_date = models.DateField()
    date_updated = models.DateField()
    total_price = models.FloatField()
    tax = models.FloatField()
    # picture = models.TextField(
    #         db_column='data',
    #         blank=True)

    def set_data(self, data):
        self._data = base64.encodestring(data)

    def get_data(self):
        return base64.decodestring(self._data)

    data = property(get_data, set_data)

    def __str__(self):
        return self.receipt_id

    # def delete(self):
    #     self.delete()