from rest_framework import serializers as s

from my_app.models import Event
from users.models import TgUser


class EventSerializer(s.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'event_name', 'event_date', 'event_location', 'event_description']

class TgUserSerializer(s.ModelSerializer):
    class Meta:
        model = TgUser
        fields = ['id', 'tg_id', 'role', 'name', 'contact', 'events']