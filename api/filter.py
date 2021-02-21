from django_filters import rest_framework as filters
from django_filters.rest_framework import FilterSet

from api.models import Title


class TitleFilter(FilterSet):
    genre = filters.CharFilter(field_name='genre__slug')

    class Meta:
        model = Title
        fields = ['genre',]