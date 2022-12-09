from django.contrib import admin
from django.urls import path
from .views import inicio, ver_fecha, mi_template

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio),
    path('fecha/', ver_fecha),
    path('mi-template/', mi_template),
]