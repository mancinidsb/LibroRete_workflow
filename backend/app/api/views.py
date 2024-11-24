from django.shortcuts import render

from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Usuario, Perfil
from rest_framework.decorators import api_view
from rest_framework import serializers
from .serializers import UsuarioSerializer, PerfilSerializer
from rest_framework.response import Response


@api_view(['GET'])
def get_by_nick(request, nick):
#Retorna o perfil do usuário com base no nome de usuário(nickname) 
    try:
        usuario = Usuario.objects.get(username=nick)
    except:
        return Response({"message": "Usuário não encontrado"}, status=404)
    
    if request.method == 'GET':
        usuario = Usuario.objects.get(username=nick)
        perfil = Perfil.objects.get(id_usuario_perfil=usuario.id)
        serializer = PerfilSerializer(perfil)
    return Response(serializer.data)

@api_view(['GET'])
def get_user(request, nick):
    try:
        usuario = Usuario.objects.get(username=nick)
    except:
        return Response({"message": "Usuário não encontrado"}, status=404)

    if request.method == 'GET':
        usuario = Usuario.objects.get(username=nick)
        serializer = UsuarioSerializer(usuario)
    return Response(serializer.data)
  
