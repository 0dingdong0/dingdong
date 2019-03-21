from django.db import models

from .warehouse import Warehouse


class Shelf(models.Model):

    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)

    code = models.CharField(max_length=10, verbose_name="编号")
    location = models.CharField(max_length=10, verbose_name="位置")

    def __str__(self):
        return self.code + "_" + self.location + '@' + str(self.warehouse)
