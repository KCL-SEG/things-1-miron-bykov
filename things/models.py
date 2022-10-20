from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import IntegerField

class Thing(AbstractUser):
    name = models.ChardField(
        unique=True,
        blank=False,
        max_length=30,
    )

    description = models.CharField(
        unique=False,
        blank=True,
        max_length=520,
    )

    quantity = IntegerField(
        unique=False,
        blank=True,
    )