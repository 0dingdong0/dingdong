from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from .account import Account
from .address import Address
from .contact import Contact
from .company import Company


class Customer(models.Model):

    account = models.OneToOneField(Account, null=True, blank=True, on_delete=models.SET_NULL)
    addresses = GenericRelation(Address, related_query_name='customer')
    contacts = GenericRelation(Contact, related_query_name='customer')

    company = models.ForeignKey(
        Company, null=True, blank=True, on_delete=models.SET_NULL,
        related_name="contact_people",
        related_query_name="contact_person")
    origin = models.CharField("来源", max_length=30)

    def __str__(self):
        return "客户"
