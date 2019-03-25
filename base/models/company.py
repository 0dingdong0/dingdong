from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from .address import Address


class Company(models.Model):

    addresses = GenericRelation(Address, related_query_name='company')

    name = models.CharField("名称", max_length=200)

    def __str__(self):
        return "公司"
