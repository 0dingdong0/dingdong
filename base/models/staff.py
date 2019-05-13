from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from .account import Account
from .contact import Contact


class Staff(models.Model):

    account = models.OneToOneField(
        Account, related_name="staff",
        null=True, blank=True,
        on_delete=models.SET_NULL)
    contacts = GenericRelation(Contact, related_query_name='staff')

    first_name = models.CharField("编号", max_length=30)
    last_name = models.CharField("编号", max_length=150)
    email = models.EmailField("邮箱")

    class Meta:
        verbose_name = "员工"
        verbose_name_plural = "员工"

    def __str__(self):
        return "员工"
