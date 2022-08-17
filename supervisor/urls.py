from django.urls.conf import path
from django.urls.resolvers import URLPattern
from supervisor import views


urlpatterns =[
    path("register/",views.becomeSupervisor.as_view()),
    path("detail/",views.supervisorDetail.as_view())
]



