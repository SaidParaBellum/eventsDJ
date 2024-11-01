from django.urls import path

from users.views import UserRegisterAPIView, getUserByTgId, ParticipateInEventView, UnparticipateInEventView

urlpatterns = [
    path('register/', UserRegisterAPIView.as_view(), name='register'),
    path('get/<int:pk>/', getUserByTgId.as_view(), name='get_user'),
    path('event/<int:event_id>/participate/', ParticipateInEventView.as_view(), name='participate_event'),
    path('event/<int:event_id>/unparticipate/', UnparticipateInEventView.as_view(), name='unparticipate_event'),
    ]