from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.tokens import default_token_generator

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('first_name', 'last_name', 'username',
                  'bio', 'role', 'email')
        model = User


class EmailAuthSerializer(serializers.Serializer):
    email = serializers.EmailField()
    confirmation_code = serializers.CharField(max_length=100)

    def validate(self, data):
        user = get_object_or_404(User, email=data['email'])
        confirmation_code = data['confirmation_code']
        real_confirmation_code = default_token_generator.make_token(user)
        print(confirmation_code, 'vs', real_confirmation_code)
        if confirmation_code == real_confirmation_code:
            refresh = RefreshToken.for_user(user)
            return {
                'token': str(refresh.access_token),
            }


