from rest_framework import viewsets, permissions
from rest_framework import filters

from api.models import Category
from api.permissions import IsAdmin
from api.serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = [ | IsAdmin]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']