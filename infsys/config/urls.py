from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import core.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(core.urls, namespace='core')),
    path('', include('core.urls')),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL,
    document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)