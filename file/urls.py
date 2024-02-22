from django.urls import path

from file.views import generate_csv

urlpatterns = [
    path("files/generate/", generate_csv),
]
