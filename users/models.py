from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class TgUser(models.Model):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )
    tg_id = models.IntegerField(primary_key=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=20, null=True, blank=True)
    events = models.ManyToManyField('my_app.Event', related_name='users')

    REQUIRED_FIELDS = ['tg_id', 'role', 'name']
    def __str__(self):
        return self.name