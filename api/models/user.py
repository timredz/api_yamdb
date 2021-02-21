from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('user', 'user'),
        ('moderator', 'moderator'),
        ('admin', 'admin')
    )

    role = models.CharField(
        choices=USER_TYPE_CHOICES,
        default='user',
        max_length=10
    )

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    bio = models.TextField(blank=True)

    REQUIRED_FIELDS = ['email']

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.email
