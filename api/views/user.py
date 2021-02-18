from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from api.utils import email_is_valid, send_email
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework import filters, viewsets
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from api.permissions import IsAdmin
from api.serializers.user import UserSerializer


User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [IsAdminUser | IsAdmin]
    serializer_class = UserSerializer
    lookup_field = 'username'
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', ]

    @action(methods=['patch', 'get'],
            detail=False,
            permission_classes=[IsAuthenticated],
            url_path='me', url_name='me')
    def me(self, request, *args, **kwargs):
        instance = self.request.user
        serializer = self.get_serializer(instance)
        if self.request.method == 'PATCH':
            serializer = self.get_serializer(
                instance, data=request.data, partial=True)
            serializer.is_valid()
            serializer.save()
        return Response(serializer.data)



@api_view(['POST'])
@permission_classes([AllowAny])
def send_confirmation_code(request):
    email = request.data.get('email')
    if email is None:
        message = 'Email is required'
    else:
        if email_is_valid(email):
            user = get_object_or_404(User, email=email)
            print('--->', email, user)
            confirmation_code = default_token_generator.make_token(user)

            send_email(email, confirmation_code)
            user.confirmation_code = confirmation_code
            message = email
            user.save()
        else:
            message = 'Valid email is required'
    return Response({'email': message})