from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from drugstore.views import ClientesViewSet

router = routers.DefaultRouter()
router.register('clientes', ClientesViewSet, basename='Clientes')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls) ),
]
