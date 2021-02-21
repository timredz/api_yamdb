from api.models.title import Title
from rest_framework import viewsets, permissions
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from api.models import Review, Comment, Title
from api.serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = PageNumberPagination
    http_method_names = ('GET', 'POST')

    def get_queryset(self):
        review = get_object_or_404(
            Review,
            # title=self.kwargs.get("title_id"),
            pk=self.kwargs.get("review_id")
        )
        return review.comments.all()

    def perform_create(self, serializer):
        get_object_or_404(
            Review,
            title=self.kwargs.get("title_id"),
            pk=self.kwargs.get("review_id")
        )
        serializer.save(author=self.request.user)
