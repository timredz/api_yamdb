from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'user'),
        (2, 'moderator'),
        (3, 'admin')
    )

    role = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=1)

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    bio = models.TextField(blank=True)

    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username