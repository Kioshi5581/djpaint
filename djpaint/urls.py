from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from paint.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', paint),
    path('files/', files),
    path('search/', search),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
