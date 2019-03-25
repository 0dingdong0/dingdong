from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from .account import Account
from .contact import Contact


class Staff(models.Model):

    account = models.OneToOneField(Account, null=True, blank=True, on_delete=models.SET_NULL)
    contacts = GenericRelation(Contact, related_query_name='staff')

    class Meta:
        verbose_name = "员工"
        verbose_name_plural = "员工"

    def __str__(self):
        return "员工"
