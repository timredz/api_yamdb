from rest_framework import serializers

from api.models import Review, Title
# from api.serializers import TitleSerializerGet


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )
    title = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name',
    )
    # ---------- при обращении к TitleSerializerGet ВАЛИТ ТЕСТ ------------
    # title = TitleSerializerGet(read_only=True)
    # title = serializers.SlugRelatedField(
    #    default=TitleSerializerGet(),
    #    queryset=Title.objects.all(),
    #    slug_field='name',
    # )

    def validate(self, data):
        if Review.objects.filter(
            title=self.context['view'].kwargs.get('title_id'),
            author=self.context['request']._user,
        ).exists():
            raise serializers.ValidationError(
                'На одно произведение, только один отзыв'
            )
        score = data['score']
        if score <= 0 or score > 10:
            raise serializers.ValidationError(
                'Оценка должна быть от 1 to 10'
            )
        return data

    class Meta:
        fields = '__all__'
        model = Review
        read_only_fields = ('title', 'author')
        # -------------- Валидатор НЕ РАБОЧИЙ -валит тест ------------------
        # validators = [serializers.UniqueTogetherValidator(
        #    queryset=Review.objects.all(),
        #    fields=['title', 'author']
        # )]
