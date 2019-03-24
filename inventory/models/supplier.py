from django.db import models


class Supplier(models.Model):

    name = models.CharField("名称", max_length=20)
    address = models.CharField("地址", max_length=200)
    contacts = models.CharField("联系人", max_length=10)

    def __str__(self):
        return self.name
