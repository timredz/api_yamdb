from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .permissions import IsAdmin, IsModerator, IsOwner, IsUser


class CustomMixin(viewsets.ModelViewSet):
    permission_types = [IsOwner]
    permission_types_dict = {
        'list': [AllowAny],
        'create': [IsUser | IsAdmin | IsModerator],
        'retrieve': [AllowAny],
        'partial_update': [IsOwner],
        'destroy': [IsAdmin | IsModerator]
    }

    def get_permissions(self):
        return [permission()
                for permission in self.permission_types_dict.get(self.action)]
