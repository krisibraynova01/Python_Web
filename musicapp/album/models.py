from django.core.validators import MinValueValidator
from django.db import models
from musicapp.profiles.models import Profile

# Create your models here.
class Album(models.Model):
    album_name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        unique=True
    )
    artist = models.CharField(max_length=30,
                              null=False,
                              blank=False)
    genre = models.CharField(max_length=30,
                             choices=(
                                 ('Pop Music', 'Pop Music'),
                                 ('Jazz Music', 'Jazz Music'),
                                 ('R&B Music', 'R&B Music'),
                                 ('Rock Music', 'Rock Music'),
                                 ('Country Music', 'Country Music'),
                                 ('Dance Music', 'Dance Music'),
                                 ('Hip Hop Music', 'Hip Hop Music'),
                                 ('Other', 'Other')
                             ),
                             null=False,
                             blank=False)
    description = models.TextField(
        null=True,
        blank=True
    )
    image_url = models.URLField(null=False, blank=False)
    price = models.FloatField(null=False,
                              blank=False,
                              validators=[
                                  MinValueValidator(0.0)
                              ])
    owner = models.ForeignKey(Profile,on_delete=models.DO_NOTHING,
                              related_name='owner_albums')

