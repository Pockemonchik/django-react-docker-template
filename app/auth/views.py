import logging
from rest_framework.response import Response
from django.http import JsonResponse
from drf_yasg.utils import swagger_auto_schema
from core.views import BaseView
from .serializers import *
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


logger = logging.getLogger(__name__)


class AuthView(ObtainAuthToken):
    """Класс для авторизации пользователя"""

    @swagger_auto_schema(responses={200: UserSerializer}, request_body=UserSerializer)
    def post(self, request):
        """Авторизация пользователя"""
        # проверяем валидность данных
        serializer = UserSerializer(data=request.data,
                                    context={'request': request})
        serializer.is_valid(raise_exception=True)
        req_user = serializer.validated_data['user']
        req_pass = serializer.validated_data['password']

        # если пользователь есть в базе то проверяем пароль и выдаем токен
        user = User.objects.filter(
            username=req_user).first()

        if user:
            auth = authenticate(username=req_user, password=req_pass)
            if auth is not None:
                token, created = Token.objects.get_or_create(user=user)
                return Response({
                    'token': token.key})
            else:
                return JsonResponse({'error': "Неверный пароль"}, status=400)
  