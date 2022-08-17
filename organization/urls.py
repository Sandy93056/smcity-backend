from django.urls.conf import path
from django.urls.resolvers import URLPattern
from organization import views

urlpatterns =[
    path("register/",views.becomeOrganization.as_view()),
    path("detail/",views.organizationdetail.as_view())
]




