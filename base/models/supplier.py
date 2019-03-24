from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

from .address import Address
from .contact_person import ContactPerson


class Supplier(models.Model):

    addresses = GenericRelation(Address, related_query_name='addresses')
    contact_people = GenericRelation(ContactPerson, related_query_name='contact_people')

    name = models.CharField(max_length=20, verbose_name="名称")

    def __str__(self):
        return self.name
