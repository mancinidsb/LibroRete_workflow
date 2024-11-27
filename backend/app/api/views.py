from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import serializers as srl
from . import models as mdl


@api_view(['GET'])
def get_by_nick(request, nick):
#Retorna o perfil do usuário com base no nome de usuário(nickname) 
    try:
        usuario = mdl.Usuario.objects.get(username=nick)
    except:
        return Response({"message": "Usuário não encontrado"}, status=404)
    
    if request.method == 'GET':
        usuario = mdl.Usuario.objects.get(username=nick)
        perfil = mdl.Perfil.objects.get(id_usuario_perfil=usuario.id)
        serializer = srl.PerfilSerializer(perfil)
    return Response(serializer.data)


@api_view(['GET'])
def get_user(request, nick):
    try:
        usuario = mdl.Usuario.objects.get(username=nick)
    except:
        return Response({"message": "Usuário não encontrado"}, status=404)

    if request.method == 'GET':
        usuario = mdl.Usuario.objects.get(username=nick)
        serializer = srl.UsuarioSerializer(usuario)
    return Response(serializer.data)
  
