from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Event
from .serializers import EventSerializer, TgUserSerializer
from rest_framework.permissions import IsAuthenticated


class EventsListView(ListAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()

class EventDetailView(RetrieveAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()

class CreateEventView(CreateAPIView):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

class UpdateEventView(UpdateAPIView):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

class DeleteEventView(DestroyAPIView):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]
    queryset = Event.objects.all()

class MyEventsListView(ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        user = self.request.user
        return user.events.all()

class GetUsersByEventView(APIView):
    def get(self, request, event_id):
        event = Event.objects.get(id=event_id)
        users = event.participants.all()
        serializer = TgUserSerializer(users, many=True)
        return Response(serializer.data)
