from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from base.models import Address


class Warehouse(models.Model):

    name = models.CharField("名称", max_length=10)
    addresses = GenericRelation(Address, related_query_name='warehouse')

    def __str__(self):
        return self.name
