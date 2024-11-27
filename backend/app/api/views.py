from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import serializers as srl
from . import models as mdl
from django.db import connection

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
  
@api_view(['GET'])
def get_user_lists(request, nick):
    try:
        with connection.cursor() as cursor:
            cursor.execute("CALL busca_listas_de_um_usuario(%s)", [nick])
            listas = cursor.fetchall()

            result = []
            for lista in listas:
                lista_nome = lista[0]
                cursor.execute("CALL busca_livros_por_username(%s)", [nick])
                livros = cursor.fetchall()

                livros_da_lista = []
                for livro in livros:
                    if livro[0] == lista_nome:
                        livros_da_lista.append(livro[2])
                
                result.append({
                    'lista': lista_nome,
                    'livros': livros_da_lista
                })

        return Response(result)
    except Exception as e:
        return Response({"message": str(e)}, status=500)