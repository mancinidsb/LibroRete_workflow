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
            listas = cursor.fetchall() # todas as listas de todos os usuários

            result = []
            # itera sobre cada lista de cada usuário
            for lista in listas:
                lista_nome = lista[0]

                cursor.execute("""
                    SELECT livro.titulo
                    FROM lista_livro
                    INNER JOIN livro ON lista_livro.isbn_livro = livro.isbn
                    INNER JOIN lista ON lista_livro.id_lista = lista.id
                    INNER JOIN perfil ON lista.id_perfil_lista = perfil.id
                    INNER JOIN usuario ON perfil.id_usuario_perfil = usuario.id
                    WHERE usuario.username = %s AND lista.nome = %s
                """, [nick, lista_nome])
                livros_da_lista = cursor.fetchall()
                
                livros_titulos = [] # todos os titulos dos livros de uma determinada lista
                for livro in livros_da_lista:
                    livros_titulos.append(livro[0])

                lista_dict = {
                    'lista': lista_nome,
                    'livros': livros_titulos
                }

                result.append(lista_dict)

        return Response(result)
    except Exception as e:
        return Response({"message": str(e)}, status=500)