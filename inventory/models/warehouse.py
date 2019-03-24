from django.db import models


class Warehouse(models.Model):

    name = models.CharField("名称", max_length=10)
    address = models.CharField("地址", max_length=200)

    def __str__(self):
        return self.name
