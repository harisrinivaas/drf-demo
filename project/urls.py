from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin

from views import homePageView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('apps.core.urls', namespace='core')),
    url(r'^helloworld/', homePageView, name='home'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

