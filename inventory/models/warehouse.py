from django.db import models


class Warehouse(models.Model):

    name = models.CharField(max_length=10, verbose_name="名称")
    address = models.CharField(max_length=200, verbose_name="地址")

    def __str__(self):
        return self.name
