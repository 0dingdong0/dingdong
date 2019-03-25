from django.db import models

from .warehouse import Warehouse


class Shelf(models.Model):

    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)

    code = models.CharField("编号", max_length=10)
    location = models.CharField("位置", null=True, blank=True, max_length=10)

    def __str__(self):
        return self.code + "_" + self.location + '@' + str(self.warehouse)
