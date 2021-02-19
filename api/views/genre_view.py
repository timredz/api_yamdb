from rest_framework import viewsets, permissions
from rest_framework import filters

from api.models import Genre
from api.permissions import IsAdmin
from api.serializers import GenreSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    # permission_classes = [ | IsAdmin]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
