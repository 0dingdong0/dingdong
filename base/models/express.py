from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from .address import Address
from .contact_person import ContactPerson


class Express(models.Model):

    addresses = GenericRelation(Address, related_query_name='addresses')
    contact_people = GenericRelation(ContactPerson, related_query_name='contact_people')

    name = models.CharField("名称", max_length=200)

    def __str__(self):
        return "快递"
