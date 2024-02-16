from django.db import models
from petstagram.photos.models import PetPhoto


# Create your models here.
class Comment(models.Model):
    comment_text = models.CharField(max_length=300,
                                    null=False,
                                    blank=False)
    date_time_of_publication = models.DateTimeField(auto_now_add=True,
                                                    blank=True,
                                                    null=True)
    to_photo = models.ForeignKey(PetPhoto, on_delete=models.CASCADE,
                                 null=False,
                                 blank=True)

class PhotoLike(models.Model):
    pet_photo = models.ForeignKey(PetPhoto, on_delete=models.CASCADE)