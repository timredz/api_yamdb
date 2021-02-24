from django.db.models import Avg, Count
from django_filters import rest_framework as filters
from rest_framework import viewsets

from api.filter import TitleFilter
from api.models import Title
from api.permissions import IsGetOrIsAdmin
from api.serializers import TitleSerializerGet, TitleSerializerPost


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    permission_classes = [IsGetOrIsAdmin]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = TitleFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TitleSerializerGet
        else:
            return TitleSerializerPost
