from django.db import transaction

from movie.exceptions import CreateUserException
from movie.models import User
from django.utils.translation import ugettext_lazy as _

from rest_framework import status, generics
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from movie.serializers import UserCreateSerializer
from movie.services import UserService


class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.none()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        try:
            with transaction.atomic():
                user = UserService().create_user(request.data)
                token, created = Token.objects.get_or_create(user=user)
        except CreateUserException as e:
            raise CreateUserException(_("Error creating user"))

        return Response(
            {
                'token': token.key,
                'first_name': user.first_name,
                'last_name': user.last_name,
            }
        )