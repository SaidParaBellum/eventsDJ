from django.contrib.auth.hashers import make_password
from rest_framework import serializers as s

from users.models import TgUser


class UserSerializer(s.ModelSerializer):

    class Meta:
        model = TgUser
        fields = ['name', 'tg_id', 'role']
        read_only_fields = ['role']



