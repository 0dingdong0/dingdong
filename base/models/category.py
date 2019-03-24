from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children')

    class Meta:
        unique_together = ('slug', 'parent',)    #enforcing that there can not be two
        verbose_name_plural = "categories"       #categories under a parent with same
                                                 #slug

    def __str__(self):                           # __str__ method elaborated later in
        full_path = [self.name]                  # post.  use __unicode__ in place of
                                                 # __str__ if you are using python 2
        k = self.parent
