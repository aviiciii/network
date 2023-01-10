from django.urls import path

from . import views

urlpatterns = [
    path("", views.following_feed, name="followingfeed"),
    
]