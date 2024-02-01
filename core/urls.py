

from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index'),
]
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('robobot/', include('core.urls')),
]
