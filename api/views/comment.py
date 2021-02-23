from rest_framework.generics import get_object_or_404

from api.mixins import CustomMixin
from api.models import Review, Comment
from api.models.title import Title
from api.serializers import CommentSerializer


class CommentViewSet(CustomMixin):
    serializer_class = CommentSerializer

    def get_queryset(self):
        queryset = Comment.objects.filter(
            review__id=self.kwargs.get('review_id')
        )
        return queryset

    def perform_create(self, serializer):
        title = get_object_or_404(Title, id=self.kwargs.get("title_id"))
        review = get_object_or_404(
            Review,
            title=title,
            id=self.kwargs.get("review_id")
        )
        serializer.save(review=review, author=self.request.user)
