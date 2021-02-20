from rest_framework import viewsets, permissions
from rest_framework import filters, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly


from api.models import Genre
from api.permissions import IsAdmin
from api.serializers import GenreSerializer


class GenreViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAuthenticatedOrReadOnly | IsAdmin]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    lookup_field = 'slug'
