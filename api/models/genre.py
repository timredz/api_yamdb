from django.db import models


class Genre(models.Model):
    name = models.CharField(
        verbose_name='Произведение',
        max_length=100,
    )
    slug = models.SlugField(
        unique=True,
        max_length=40,
        verbose_name='Поле slug жанра',
        help_text='Не более 40 символов',
    )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f'{self.name[:15]}'
