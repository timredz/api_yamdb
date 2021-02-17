from django.db import models

from .review import Review
from .user import User


class Comment(models.Model):
    id = models.IntegerField(
        "ID комментария",
        db_index=True,
        primary_key=True
    )
    text = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name="Текст комментария",
        help_text='Оставте свой комментарий'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name="username автора комментария"
    )
    pub_date = models.DateTimeField(
        "Дата публикации комментария",
        auto_now_add=True,
        db_index=True
    )

    def __str__(self):
        return self.text
