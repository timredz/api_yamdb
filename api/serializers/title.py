from django.shortcuts import get_object_or_404
from rest_framework import serializers

from api.models import Title, Genre, Category
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
        reviews = obj.reviews.all()
        count = len(reviews)
        if count == 0:
            return None
        else:
            score_sum = 0
            for review in reviews:
                score_sum += review.score
            rating = round(score_sum/count)
            return rating






