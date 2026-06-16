from django.urls import path

from . import views

app_name = "beranda"

urlpatterns = [
    path("", views.index, name="index"),
]
