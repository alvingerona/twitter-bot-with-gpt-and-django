from django.urls import path
from . import views

urlpatterns = [
    path(route='generate/tweets', view=views.generateTweets),
]
