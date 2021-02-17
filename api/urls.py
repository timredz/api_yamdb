from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views.user import UserViewSet, send_confirmation_code

from .serializers.user import EmailAuthSerializer

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

v1_router = DefaultRouter()
v1_router.register(r'users', UserViewSet)

urlpatterns = [
    path('v1/auth/email/', send_confirmation_code),
    path('v1/token/',
         TokenObtainPairView.as_view(serializer_class=EmailAuthSerializer),
         name='token_obtain_pair'
    ),
    path('v1/token/refresh/',
         TokenRefreshView.as_view(),
         name='token_refresh'
    ),
    path('v1/', include(v1_router.urls)),
]
