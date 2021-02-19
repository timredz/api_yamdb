from rest_framework import viewsets, permissions
from rest_framework import filters

from api.models import Title
from api.serializers import TitleSerializer


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = ()
    filter_backends = [filters.SearchFilter]
    filterset_fields = ['name', 'year', 'genre__slug', 'category__slug']