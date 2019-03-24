from django.db import models

from .supplier import Supplier
from .category import Category


class Article(models.Model):

    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True, blank=True)

    code = models.CharField("编号", max_length="10")
    name = models.CharField("名字", max_length=20)

    def __str__(self):
        return self.code + '_' + self.name

