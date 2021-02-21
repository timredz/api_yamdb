from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import viewsets, permissions
from django_filters import rest_framework as filters

from api.filter import TitleFilter
from api.models import Title, Genre, Category
from api.serializers import TitleSerializerPost, TitleSerializerGet
from api.permissions import IsAdmin, IsGetOrIsAdmin


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    permission_classes = [IsGetOrIsAdmin]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = TitleFilter
    #
    # def perform_create(self, serializer):
    #     category = get_object_or_404(Category, slug=self.request.data['category'])
    #     serializer.save(category=category)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TitleSerializerGet
        else:
            return TitleSerializerPost

