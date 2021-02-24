from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from .title import Title
from .user import User


class Review(models.Model):
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
    score = models.PositiveSmallIntegerField(
        validators=(MinValueValidator(1), MaxValueValidator(10)),
        default=1,
        verbose_name="Оценка",
        help_text="Добавте свою оценку (от 1 до 10)"
    )
    pub_date = models.DateTimeField(
        verbose_name="Дата публикации отзыва",
        db_index=True,
        auto_now_add=True
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
