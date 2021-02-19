from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions
from rest_framework import filters

from api.models import Title, Genre, Category
from api.serializers import TitleSerializer


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = ()
    filter_backends = [filters.SearchFilter]
    filterset_fields = ['name', 'year', 'genre__slug', 'category__slug']

    def perform_create(self, serializer):
        category = get_object_or_404(Category, slug=self.request.data['category'])
        serializer.save(category=category)

