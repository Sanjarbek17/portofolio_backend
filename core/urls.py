from django.contrib import admin
from django.urls import path, include
# add media
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls'), name='portfolio')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
