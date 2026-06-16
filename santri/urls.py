from django.urls import path

from . import views

app_name = "santri"

urlpatterns = [
    path("", views.student_list, name="list"),
    path("tambah/", views.student_create, name="create"),
    path("edit/<int:pk>/", views.student_update, name="update"),
    path("hapus/<int:pk>/", views.student_delete, name="delete"),


]
