from django.db import models

from .supplier import Supplier
from .article_category import ArticleCategory


class Article(models.Model):

    supplier = models.ForeignKey(
        Supplier,
        null=True, blank=True,
        related_name="articles",
        related_query_name="article",
        on_delete=models.CASCADE)
    category = models.ForeignKey(
        ArticleCategory,
        null=True, blank=True,
        related_name="articles",
        related_query_name="article",
        on_delete=models.CASCADE)

    code = models.CharField("编号", max_length="10")
    name = models.CharField("名字", max_length=20)

    def __str__(self):
        return self.code + '_' + self.name
