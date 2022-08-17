from device.views import deviceapi
from django.urls import path
from device import views
urlpatterns = [
    path("api/",deviceapi.as_view() ),
    path("nearbydevice/", views.near.as_view()),
    path("api/restricted/", views.AddDeviceRestricted.as_view()),
    path("availableweb/",views.alldeviceweb),
]