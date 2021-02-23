from rest_framework.generics import get_object_or_404

from api.mixins import CustomMixin
from api.models import Title
from api.serializers import ReviewSerializer


class ReviewViewSet(CustomMixin):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        title = get_object_or_404(Title, id=self.kwargs.get("title_id"))
        return title.reviews.all()

    def perform_create(self, serializer):
        title = get_object_or_404(Title, id=self.kwargs.get("title_id"))
        serializer.save(title=title, author=self.request.user)
