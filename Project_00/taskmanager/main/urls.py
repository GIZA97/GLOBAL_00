from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='house'),
    path('dogs', views.about, name='about'),
    path('story', views.create, name='create'),
]
