from rest_framework import viewsets, permissions
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from api.models import Review, Title
from api.serializers import ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticatedOrReadOnly)

    pagination_class = PageNumberPagination
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['name', 'year', 'genre__slug', 'category__slug']

    def get_queryset(self):
        title = get_object_or_404(Title, pk=self.kwargs.get("title_id"))
        return title.reviews

    def perform_create(self, serializer):
        get_object_or_404(Title, pk=self.kwargs.get("title_id"))
        serializer.save(author=self.request.user)
