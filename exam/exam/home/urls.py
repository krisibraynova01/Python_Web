from django.urls import path

from exam.home.views import index

urlpatterns = (
    path('',index,name='index'),
)