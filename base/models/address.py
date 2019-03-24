from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Address(models.Model):

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    address = models.CharField("地址", max_length=360)
    postal_code = models.CharField("邮编", max_length=10, blank=True)
    contact_person = models.CharField("联系人", max_length=50, black=True)
    contact_phone1 = models.CharField("联系电话", max_length=15, black=True)
    contact_phone2 = models.CharField("联系电话", max_length=15, black=True)

    def __str__(self):
        return "Address: " + self.postal_code + ' ' + self.contact_person
