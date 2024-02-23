from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models


# Create your models here.

def validate_username(username):
    if not username.isalnum() or '_' in username:
        raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")


class Profile(models.Model):
    username = models.CharField(max_length=15,
                                blank=False,
                                null=False,
                                validators=[
                                    MinLengthValidator(2),
                                    validate_username
                                ])
    email = models.EmailField(null=False, blank=False)
    age = models.PositiveIntegerField(
        blank=True,
        null=True
    )
