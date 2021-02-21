from rest_framework import viewsets
from rest_framework import filters, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser


from api.models import Genre
from api.permissions import IsAdmin, IsGetOrIsAdmin
from api.serializers import GenreSerializer


class GenreViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsGetOrIsAdmin]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    lookup_field = 'slug'
