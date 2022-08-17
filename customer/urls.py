from django.urls import path
from . import views
from django.urls.resolvers import URLPattern
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path("gettoken/",obtain_auth_token),
    path("register/",views.user_register.as_view()),
    # path("login/", views.user_login.as_view()),
    # path("temp/", views.temp),
    # path("gettokenz/", views.gettokenz.as_view()),
    path("userprofile/", views.user_profile_api.as_view()),
    path("register/restricted/", views.UserRegisterRestricted.as_view()),

]