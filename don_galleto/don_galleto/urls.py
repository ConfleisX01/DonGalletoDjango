from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('panel', views.panel, name='panel'),
    path('admin/', admin.site.urls),
    path('panel/clientes/', include('clientes_app.urls'),),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
