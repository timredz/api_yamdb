from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from api.models import Review, Title
from api.serializers import ReviewSerializer
from api.permissions import IsAuthorOrReadOnly


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    # pagination_class = PageNumberPagination
    # http_method_names = ('GET', 'POST')

    def get_queryset(self):
        title = get_object_or_404(Title, id=self.kwargs.get("title_id"))
        return title.reviews

    def perform_create(self, serializer):
        title = get_object_or_404(Title, id=self.kwargs.get("title_id"))
        # serializer.save(author=self.request.user)
        serializer.save(title=title)


class Review_IDViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    pagination_class = PageNumberPagination
    http_method_names = ('GET', 'POST', 'DELETE')

    def get_queryset(self):
        review = get_object_or_404(
            Review,
            title=self.kwargs.get("title_id"),
            pk=self.kwargs.get("rewiew_id")
        )
        return review

    def perform_create(self, serializer):
        get_object_or_404(
            Review,
            title=self.kwargs.get("title_id"),
            pk=self.kwargs.get("rewiew_id")
        )
        serializer.save(author=self.request.user)
