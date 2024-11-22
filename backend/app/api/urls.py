from rest_framework.routers import DefaultRouter
from django.urls import path
from . import views
from .views import *


# router = DefaultRouter()
# router.register(r'usuarios', UsuarioViewSet, basename='usuario')
# router.register(r'perfis/<str:nick>', PerfilViewSet, basename='perfil')
# urlpatterns = router.urls

urlpatterns = [
    path('usuarios/',views.get_users, name='usuarios'),
    
]
