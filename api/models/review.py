from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from .title import Title
from .user import User


class Review(models.Model):
    id = models.IntegerField("ID  отзыва", primary_key=True)
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name="id публикации",
    )
    text = models.TextField(
        verbose_name="Текст отзыва",
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

    class Meta:
        ordering = ['-pub_date']
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'title'],
                name='unique_review'
            ),
        ]
