from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('documentation/', include('docs.urls')),
    path('404/', include('base.urls')),
]
