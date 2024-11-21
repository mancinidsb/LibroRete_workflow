from django.shortcuts import render

from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Usuario, Perfil
from rest_framework.decorators import api_view
from rest_framework import serializers
from .serializers import UsuarioSerializer, PerfilSerializer
from rest_framework.response import Response

class UsuarioViewSet(ReadOnlyModelViewSet): 
  queryset = Usuario.objects.all() # Consulta todos os usuários 
  serializer_class = UsuarioSerializer

@api_view(['GET'])
def get_by_nick(request, nick):
  
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
def get_users(request):
    if request.method == 'GET':
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
    return Response(serializer.data)
  

# class PerfilViewSet(ReadOnlyModelViewSet):
#   queryset = Perfil.objects.all() # Consulta todos os perfis
#   serializer_class = PerfilSerializer
#   def get_queryset(self):
#     queryset = Perfil.objects.all()
#     nick = self.kwargs['nick']
#     if nick:
#       usuario = Usuario.objects.get(username=nick)
#       queryset = queryset.filter(id_usuario_perfil=usuario.id)
#     return queryset