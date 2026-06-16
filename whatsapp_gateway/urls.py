from django.urls import path

from . import views

app_name = "whatsapp_gateway"

urlpatterns = [

    path("",views.log_list,name="list"),
    path( "setting/", views.whatsapp_setting, name="setting" ),
]