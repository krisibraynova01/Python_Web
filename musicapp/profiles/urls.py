from django.urls import path

from musicapp.profiles.views import profile_details, profile_delete

urlpatterns = (
    path('details',profile_details,name='profile_details'),
    path('delete/',profile_delete,name='delete_profile')
)