from django.shortcuts import render
from rest_framework.generics import  RetrieveAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from my_app.models import Event
from users.models import TgUser
from users.serializers import UserSerializer


# Create your views here.

class UserRegisterAPIView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = TgUser.objects.all()

class getUserByTgId(RetrieveAPIView):
    serializer_class = UserSerializer
    def get(self, request, tg_id):
        user = TgUser.objects.filter(tg_id=tg_id).first()
        if user.role == "admin":
            return Response({"error": "Админы не могут быть получены"}, status=403)
        if user:
            return Response(UserSerializer(user).data)
        return Response({"error": "Пользователь не найден"}, status=404)



class ParticipateInEventView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, event_id):
        user = TgUser.objects.get(tg_id=request.user.tg_id)
        try:
            event = Event.objects.get(id=event_id)
            user.events.add(event)
            return Response({"message": "Участие в событии подтверждено"})
        except Event.DoesNotExist:
            return Response({"error": "Событие не найдено"}, status=404)

class UnparticipateInEventView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, event_id):
        user = TgUser.objects.get(tg_id=request.user.tg_id)
        try:
            event = Event.objects.get(id=event_id)
            user.events.remove(event)
            return Response({"message": "Вы отказались от участия в событии"})
        except Event.DoesNotExist:
            return Response({"error": "Событие не найдено"}, status=404)