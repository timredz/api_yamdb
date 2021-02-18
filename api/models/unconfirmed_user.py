from django.db import models


class UnconfirmedUser(models.Model):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    confirmation_code = models.CharField(
        verbose_name='confirmation code',
        max_length=30,
    )

    def __str__(self):
        return f'{self.email} '
