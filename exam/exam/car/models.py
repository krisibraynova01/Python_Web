from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models

from exam.profiles.models import Profile


# Create your models here.
class Car(models.Model):
    type = models.CharField(
        max_length=10,
        null=False,
        blank=False,
        choices=
        (
            ('Rally', 'Rally'),
            ('Open-wheel', 'Open-wheel'),
            ('Kart', 'Kart'),
            ('Drag', 'Drag'),
            ('Other', 'Other')
        )
    )
    model = models.CharField(
        max_length=15,
        null=False,
        blank=False,
        validators=[
            MinLengthValidator(1)
        ]
    )
    year = models.IntegerField(
        null=False,
        blank=False,
        validators=
        [
            MinValueValidator(1999, message="Year must be between 1999 and 2030!"),
            MaxValueValidator(2030, message="Year must be between 1999 and 2030!")
        ]
    )
    image_url = models.URLField(
        unique=True,
        null=False,
        blank=False,
        error_messages={
            'unique': 'This image URL is already in use! Provide a new one.',
        }
    )
    price = models.FloatField(
        null=False,
        blank=False,
        validators=[
            MinValueValidator(1.0)
        ]
    )
    owner = models.ForeignKey(Profile,on_delete=models.CASCADE, related_name='cars_profile')
