from django.shortcuts import get_object_or_404
from rest_framework import serializers

from api.models import Title, Genre, Category
from api.serializers import CategorySerializer


class TitleSerializer(serializers.ModelSerializer):

    genre = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Genre.objects.all(),
        default=serializers.CurrentUserDefault(),
        many=True
    )
    rating = serializers.SerializerMethodField(method_name=None)
    category = CategorySerializer(read_only=True)

    class Meta:
        fields = '__all__'
        model = Title

    def get_rating(self, obj):
        title = get_object_or_404(Title, pk=self.initial_data['title_id'])
        reviews = title.reviews.all()
        for review in reviews:
            if review.count():
                score_avg = (sum(review.score)) / review.count()
                return score_avg
            return None






