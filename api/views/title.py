from django_filters import rest_framework as filters
from rest_framework import viewsets

from api.filter import TitleFilter
from api.models import Title
from api.permissions import IsGetOrIsAdmin
from api.serializers import TitleSerializerGet, TitleSerializerPost


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
<<<<<<< HEAD
    serializer_class = TitleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    filterset_fields = ['name', 'year', 'genre__slug', 'category__slug']

    def perform_create(self, serializer):
        category = get_object_or_404(Category, slug=self.request.data['category'])
        serializer.save(category=category)
=======
    permission_classes = [IsGetOrIsAdmin]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = TitleFilter
>>>>>>> 146d64b718055d8b3d2dd604726d1c2701d5c51a

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TitleSerializerGet
        else:
            return TitleSerializerPost
