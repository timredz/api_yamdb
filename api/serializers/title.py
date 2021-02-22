from django.db.models import Avg
from rest_framework import serializers

from api.models import Category, Genre, Title
from api.serializers import CategorySerializer, GenreSerializer


class TitleSerializerPost(serializers.ModelSerializer):

    genre = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Genre.objects.all(),
        default=serializers.CurrentUserDefault(),
        many=True
    )

    category = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Category.objects.all(),
        default=CategorySerializer(),
    )

    class Meta:
        fields = '__all__'
        model = Title


class TitleSerializerGet(serializers.ModelSerializer):

    genre = GenreSerializer(many=True)
    rating = serializers.SerializerMethodField()
    category = CategorySerializer(read_only=True)

    class Meta:
        fields = '__all__'
        model = Title

    def get_rating(self, obj):
        if len(obj.reviews.all()) == 0:
            return None
        return obj.reviews.aggregate(round(Avg('score')))
