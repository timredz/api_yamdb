from rest_framework import serializers

from api.models import Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        exclude = ('id',)
        model = Category
