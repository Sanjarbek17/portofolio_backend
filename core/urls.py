from django.contrib import admin
from django.urls import path, include
# add media
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from django.views.static import serve
import os

from .views import download_text_file

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FLUTTER_WEB_APP = os.path.join(BASE_DIR, 'portfolio_template')

def flutter_redirect(request, resource):
    return serve(request, resource, FLUTTER_WEB_APP)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda r: flutter_redirect(r, 'index.html')),
    path('portfolio_template/<path:resource>', flutter_redirect),
    path('test/', download_text_file),
    path('', include('portfolio.urls'), name='portfolio'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
