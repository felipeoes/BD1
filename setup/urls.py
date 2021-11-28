from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from drugstore.views import *

router = routers.DefaultRouter()
router.register('clientes', ClientesViewSet, basename='Clientes')
router.register('clientes-telefones', ClientesTelefonesViewSet, basename='ClientesTelefones')
router.register('programa-beneficios', ProgramasBeneficiosViewSet, basename='ProgramaBeneficios')
router.register('funcionarios', FuncionariosViewSet, basename='Funcionarios')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls) ),
]
