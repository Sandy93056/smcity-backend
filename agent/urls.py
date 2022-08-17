from django.urls.conf import path
from django.urls.resolvers import URLPattern
from agent import views

urlpatterns =[
    path("register/",views.becomeAgent.as_view()),
    path("detail/",views.agentdetail.as_view())
]




