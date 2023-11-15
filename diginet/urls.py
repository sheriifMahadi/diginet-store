from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from main.views import home, about

urlpatterns = [
    path('about', about, name="about"),
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('', include('stores.urls')),
    path('', home, name="homepage"),
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
