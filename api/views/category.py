from rest_framework import filters, viewsets

from api.mixins import CreateListDestroyMixin
from api.models import Category
from api.permissions import IsGetOrIsAdmin
from api.serializers import CategorySerializer


class CategoryViewSet(CreateListDestroyMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsGetOrIsAdmin]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    lookup_field = 'slug'
