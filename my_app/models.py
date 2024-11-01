from django.db import models

# Create your models here.

class Event(models.Model):
    event_name = models.CharField(max_length=200)
    event_date = models.DateTimeField()
    event_location = models.CharField(max_length=200)
    event_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.event_name

