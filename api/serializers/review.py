from rest_framework import serializers

from api.models import Review, Title


# class CurrentTitleDefault:
#    requires_context = True
#
#    def __call__(self, serializer_field):
#        print(serializer_field.context['request'])


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    title = serializers.SlugRelatedField(
        queryset=Title.objects.all(),
        slug_field='name'
    )

    def validate(self, data):
        score = data['score']
        if score <= 0 or score > 10:
            raise serializers.ValidationError(
                'Оценка должна быть от 1 to 10'
            )
        return data

    class Meta:
        fields = '__all__'
        model = Review
        validators = [serializers.UniqueTogetherValidator(
            queryset=Review.objects.all(),
            fields=['title', 'author']
        )]
