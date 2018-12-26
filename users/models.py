from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('Unregistered', 'Unregistered'),
        ('Player', 'Player'),
        ('Coach', 'Coach'),
        ('Director', 'Director'),
        ('Agent', 'Agent'),
        ('Referee', 'Referee'),
    )
    user_type = models.CharField(max_length=100, help_text='First Name', choices=USER_TYPE_CHOICES, default='Unregistered')
