from rest_framework.generics import get_object_or_404

from api.mixins import CustomMixin
from api.models import Review
from api.serializers import CommentSerializer


class CommentViewSet(CustomMixin):
    serializer_class = CommentSerializer

    def get_queryset(self):
        review = get_object_or_404(
            Review, id=self.kwargs.get('review_id')
        )
        return review.comments.all()

    def perform_create(self, serializer):
        review = get_object_or_404(
            Review,
            title=self.kwargs.get("title_id"),
            id=self.kwargs.get("review_id")
        )
        serializer.save(review=review, author=self.request.user)
