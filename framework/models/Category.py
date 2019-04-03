from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.name


