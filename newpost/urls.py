from django.urls import path

from . import views

urlpatterns = [
    path("", views.newpost, name="newpost"),
    
]