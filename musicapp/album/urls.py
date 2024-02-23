from django.urls import path, include

from musicapp.album.views import add_album, details_album, edit_album, delete_album

urlpatterns = (
    path('add/',add_album,name='add_album'),
    path('<int:pk>/',include([
         path('details/',details_album,name='details_album'),
         path('edit/',edit_album,name='edit_album'),
         path('delete/',delete_album, name='delete_album'),

])
         ))