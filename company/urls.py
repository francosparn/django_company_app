from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('', include('applications.employees.urls')),
    re_path('', include('applications.departments.urls')),
    #re_path('', include('applications.customers.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
