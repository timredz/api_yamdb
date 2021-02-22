from django.db import models

from .category import Category
from .genre import Genre


class Title(models.Model):
    id = models.IntegerField("ID произведения", primary_key=True)
    name = models.CharField(
        verbose_name='Произведение',
        max_length=100,
    )
    year = models.IntegerField(
        verbose_name="Год выпуска"
    )
    description = models.TextField(
        blank=True,
        verbose_name='Описание',
    )
    genre = models.ManyToManyField(
        Genre,
        through='GenreTitleRelations',
        blank=True,
        related_name='titles',
        verbose_name="Жанр",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='titles',
        verbose_name="Категория",
    )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f'{self.name[:15]} {self.year} '


class GenreTitleRelations(models.Model):
    genre = models.ForeignKey(
        Genre,
        null=True,
        on_delete=models.SET_NULL
    )
    title = models.ForeignKey(
        Title,
        null=True,
        on_delete=models.SET_NULL
    )
