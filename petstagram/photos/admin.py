from django.contrib import admin
from petstagram.photos.models import PetPhoto

@admin.register(PetPhoto)
class PetPhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_of_publication', 'description', 'display_tagged_pets')

    def display_tagged_pets(self, obj):
        return ', '.join([pet.name for pet in obj.pets.all()])

    display_tagged_pets.short_description = 'Tagged Pets'
