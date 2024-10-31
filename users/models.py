from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    repeat_password = models.CharField(max_length=100)
    age = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(200)
        ]
    )

    def __str__(self):
        return self.username
