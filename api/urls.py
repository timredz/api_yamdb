from api.views.review_views import ReviewViewSet
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views.user import UserViewSet, send_confirmation_code
from api.views import CategoryViewSet, GenreViewSet, TitleViewSet

from .serializers.user import EmailAuthSerializer
from rest_framework_simplejwt.views import (
    TokenObtainPairView
)

v1_router = DefaultRouter()
v1_router.register(r'users', UserViewSet)
v1_router.register('categories', CategoryViewSet, basename='categories')
v1_router.register('genres', GenreViewSet, basename='genres')
v1_router.register('titles', TitleViewSet, basename='titles')
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)

urlpatterns = [
    path('v1/auth/email/', send_confirmation_code),
    path(
        'v1/token/',
        TokenObtainPairView.as_view(serializer_class=EmailAuthSerializer),
        name='token_obtain_pair'
    ),
    path('v1/', include(v1_router.urls)),
]
