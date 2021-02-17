from django.db import models


class Category(models.Model):
    name = models.CharField(
        verbose_name='Категория',
        max_length=100,
    )
    slug = models.SlugField(
        unique=True,
        max_length=40,
        verbose_name='Поле slug категории',
        help_text='Не более 40 символов',
    )

    def __str__(self):
        return f'{self.name[:15]} '
