from rest_framework import serializers

from api.models import Genre


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        exclude = ('id',)
        model = Genre
