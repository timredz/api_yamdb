from django.db import models

from .title import Title
from .user import User


class Review(models.Model):
    SCORE = zip(range(1, 11), range(1, 11))
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
        choices=SCORE,
        default=1,
        help_text='Добавте свою оценку (от 1 до 10)'
    )
    pub_date = models.DateTimeField(
        "Дата публикации отзыва",
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
