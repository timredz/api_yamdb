import django_filters
from django_filters import rest_framework as filters
from django_filters.rest_framework import FilterSet

from api.models import Title


class TitleFilter(FilterSet):
    genre = filters.CharFilter(field_name='genre__slug')
    category = filters.CharFilter(field_name='category__slug')
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    year = filters.NumberFilter(field_name='year')

    class Meta:
        model = Title
        fields = ['genre', 'category', 'name', 'year']