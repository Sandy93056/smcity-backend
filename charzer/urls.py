
from django.contrib import admin
from django.urls import path, include
# from djapp.views import budget

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path("customer/",include("customer.urls")),
    path("agent/",include("agent.urls")),
    path("supervisor/",include("supervisor.urls")),
    path("device/",include("device.urls")),

    path("organization/",include("organization.urls")),
    path("transaction/",include("transaction.urls")),
    # path("r", budget),
]

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)