from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):

    class Meta:
        verbose_name = "帐号"
        verbose_name_plural = "帐号"
        ordering = ['-username']

    def __str__(self):
        return "Base.account.Account - " + self.username
