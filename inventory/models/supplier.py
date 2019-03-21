from django.db import models


class Supplier(models.Model):

    name = models.CharField(max_length=20, verbose_name="名称")
    address = models.CharField(max_length=200, verbose_name="地址")
    contacts = models.CharField(max_length=10, verbose_name="联系人")

    def __str__(self):
        return self.name
