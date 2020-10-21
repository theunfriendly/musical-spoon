from django.urls import path
from .views import *
urlpatterns = [
    path('index/<str:id>',index,name='index'),
    path('success/<str:id>',success),
]