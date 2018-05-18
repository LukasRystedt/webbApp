"""Defines url patterns for learning_log"""

from django.urls import path
from . import views

app_name = "learning_log"
url_patterns = [
    #home page.
    path("", views.index, name="index")
]