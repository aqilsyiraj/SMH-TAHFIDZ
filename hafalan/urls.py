from django.urls import path

from . import views

app_name = "hafalan"

urlpatterns = [
    path("", views.setoran_list, name="list"),
    path("tambah/", views.setoran_create, name="create"),
    path("edit/<int:pk>/", views.setoran_update, name="update"),
    path("hapus/<int:pk>/", views.setoran_delete, name="delete"),

]
