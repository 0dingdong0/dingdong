from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models

from .contact import Contact


class ContactPerson(models.Model):

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    contacts = GenericRelation(Contact, related_query_name='contact_person')

    name = models.CharField(max_length=100)

    def __str__(self):
        return "联系人: " + self.name
