from django.urls import path
from .views import (
    EventsListView, EventDetailView, CreateEventView,
    UpdateEventView, DeleteEventView, MyEventsListView, GetUsersByEventView
)

urlpatterns = [
    path('events/', EventsListView.as_view(), name='events-list'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('events/create/', CreateEventView.as_view(), name='create-event'),
    path('events/update/<int:pk>/', UpdateEventView.as_view(), name='update-event'),
    path('events/delete/<int:pk>/', DeleteEventView.as_view(), name='delete-event'),
    path('my-events/', MyEventsListView.as_view(), name='my-events'),
    path('events/<int:event_id>/users/', GetUsersByEventView.as_view(), name='get-users-by-event'),
]
