from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .models import Perfil, Convite
from .serializers import PerfilSerializer, ConviteSerializer, UserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class PerfilViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Perfil.objects.select_related('user').all()
    serializer_class = PerfilSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx.update({'request': self.request})
        return ctx

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def meu_perfil(request):
    perfil = request.user.perfil
    serializer = PerfilSerializer(perfil, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def lista_convites(request):
    perfil = request.user.perfil
    convites = Convite.objects.filter(convidado=perfil, aceito=False)
    serializer = ConviteSerializer(convites, many=True, context={'request': request})
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def enviar_convite(request, perfil_id):
    solicitante = request.user.perfil
    convidado = get_object_or_404(Perfil, id=perfil_id)
    if convidado == solicitante:
        return Response({'detail': 'Não pode convidar você mesmo.'}, status=status.HTTP_400_BAD_REQUEST)
    # evita duplicatas
    convite, created = Convite.objects.get_or_create(solicitante=solicitante, convidado=convidado)
    if not created:
        return Response({'detail': 'Convite já enviado.'}, status=status.HTTP_400_BAD_REQUEST)
    serializer = ConviteSerializer(convite, context={'request': request})
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def aceitar_convite(request, convite_id):
    perfil = request.user.perfil
    convite = get_object_or_404(Convite, id=convite_id, convidado=perfil, aceito=False)
    convite.aceito = True
    convite.save()
    # adicionar contatos em ambos perfis
    perfil.contatos.add(convite.solicitante)
    convite.solicitante.contatos.add(perfil)
    return Response({'detail': 'Convite aceito.'})
