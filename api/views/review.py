from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, viewsets
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.pagination import PageNumberPagination

from api.models import Review, Title
from api.serializers import ReviewSerializer
from api.permissions import IsAuthorOrIsAdminOrReadOnly, IsGetOrIsAdmin


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticated)
    # pagination_class = PageNumberPagination
    http_method_names = ('GET', 'POST')

    def get_queryset(self):
        title = get_object_or_404(Title, id=self.kwargs.get("title_id"))
        return title.reviews

    def perform_create(self, serializer):
        title = get_object_or_404(Title, id=self.kwargs.get("title_id"))
        serializer.save(title=title, author=self.request.user)


class Review_IDViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsAuthorOrIsAdminOrReadOnly
    ]
    pagination_class = PageNumberPagination
    http_method_names = ('GET', 'PATCH', 'DELETE')

    def get_queryset(self):
        title = get_object_or_404(Title, id=self.kwargs.get("title_id"))
        review = get_object_or_404(
            Review,
            title=title,
            id=self.kwargs.get("rewiew_id")
        )
        return review

    def perform_update(self, serializer):
        title = get_object_or_404(Title, id=self.kwargs.get("title_id"))
        review = get_object_or_404(
            Review,
            title=title,
            id=self.kwargs.get("rewiew_id")
        )
        serializer.save(review=review, author=self.request.user)
