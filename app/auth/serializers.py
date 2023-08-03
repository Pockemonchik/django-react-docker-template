from rest_framework import serializers
from datetime import datetime, date

class UserSerializer(serializers.Serializer):
    user = serializers.CharField(help_text="Имя пользователя (2)")
    password = serializers.CharField(help_text="Пароль пользователя (2)")