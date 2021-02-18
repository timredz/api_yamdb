from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string
from rest_framework.response import Response
from api.utils import email_is_valid, send_email
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework import filters, viewsets
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from api.permissions import IsAdmin
from api.serializers.user import UserSerializer
from api.models import UnconfirmedUser


User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [IsAdminUser | IsAdmin]
    serializer_class = UserSerializer
    lookup_field = 'username'
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', ]

    @action(methods=['patch', 'get'], detail=False,
            permission_classes=[IsAuthenticated],
            url_path='me', url_name='me')
    def me(self, request):
        user = request.user
        serializer = self.get_serializer(user)
        if self.request.method == 'PATCH':
            serializer = self.get_serializer(
                user, data=request.data, partial=True)
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
            confirmation_code = get_random_string(length=30)
            UnconfirmedUser.objects.update_or_create(
                email=email,
                defaults={'confirmation_code': confirmation_code}
            )
            send_email(email, confirmation_code)
            message = email
        else:
            message = 'Valid email is required'
    return Response({'email': message})