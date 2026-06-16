from django.urls import path

from . import views

app_name = "laporan"

urlpatterns = [
    path("", views.report_list, name="list"),
    path("buat/", views.report_create, name="create"),
    path("edit/<int:pk>/", views.report_update, name="update"),
    path("hapus/<int:pk>/", views.report_delete, name="delete"),
    path("<int:pk>/", views.report_detail, name="detail"),
    path("<int:pk>/kirim/", views.report_send, name="send"),
]
