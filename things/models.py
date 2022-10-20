from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import IntegerField

class Thing(models.Model):
    name = models.CharField(
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