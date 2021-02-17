from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from .title import Title
from .user import User


class Review(models.Model):
    id = models.IntegerField(
        "ID отзыва",
        db_index=True,
        primary_key=True
    )
    text = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name="Текст отзыва",
        help_text='Добавте свой отзыв'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name="username пользователя"
    )
    score = models.IntegerField(
        "Оценка",
        help_text='Добавте свою оценку (от 1 до 10)',
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    pub_date = models.DateTimeField(
        "Дата публикации отзыва",
        auto_now_add=True,
        db_index=True
    )

    def __str__(self):
        return self.text
