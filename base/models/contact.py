from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Contact(models.Model):

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    type = models.CharField("联系方式", max_length=50)
    value = models.CharField("值", max_length=254)

    def __str__(self):
        return "Contact: " + self.type + ':' + self.value
