from django.db import models

from .shelf import Shelf
from .supplier import Supplier
from .entry import Entry


class Article(models.Model):

    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    shelves = models.ManyToManyField(Shelf, verbose_name="货架", through="Position")

    code = models.CharField(max_length="10", verbose_name="编号")
    name = models.CharField(max_length=20, verbose_name="名字")

    def __str__(self):
        return self.code + '_' + self.name


class Position(models.Model):

    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    shelf = models.ForeignKey(Shelf, on_delete=models.CASCADE)
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)

    quantity = models.IntegerField()

