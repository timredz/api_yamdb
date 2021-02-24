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
    rating = serializers.FloatField(read_only=True)
    genre = GenreSerializer(many=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        fields = '__all__'
        model = Title
