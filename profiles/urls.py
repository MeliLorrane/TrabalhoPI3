from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PerfilViewSet, meu_perfil, lista_convites, enviar_convite, aceitar_convite

router = DefaultRouter()
router.register(r'perfis', PerfilViewSet, basename='perfis')

urlpatterns = [
    path('', include(router.urls)),
    path('perfil/', meu_perfil, name='meu_perfil'),
    path('convites/', lista_convites, name='lista_convites'),
    path('convites/enviar/<int:perfil_id>/', enviar_convite, name='enviar_convite'),
    path('convites/aceitar/<int:convite_id>/', aceitar_convite, name='aceitar_convite'),
]
