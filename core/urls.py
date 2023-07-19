from django.contrib import admin
from django.urls import path, include
# add media
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from django.views.static import serve
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FLUTTER_WEB_APP = os.path.join(BASE_DIR, 'portfolio_template')

def flutter_redirect(request, resource):
    return serve(request, resource, FLUTTER_WEB_APP)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('portfolio_template/', lambda r: flutter_redirect(r, 'index.html')),
    path('portfolio_template/<path:resource>', flutter_redirect),
    path('', include('portfolio.urls'), name='portfolio'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
