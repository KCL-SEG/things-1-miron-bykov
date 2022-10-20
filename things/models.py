from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import IntegerField

class Thing(models.Model):
    name = models.CharField(
        max_length=30,
    )

    description = models.CharField(
    
        max_length=520,
    )

    quantity = IntegerField(

    )