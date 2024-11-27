from rest_framework import serializers
from . import models as mdl


class UsuarioSerializer(serializers.ModelSerializer): 
  class Meta: 
    model = mdl.Usuario 
    fields = '__all__' # Inclui todos os campos da tabela

class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = mdl.Perfil
        fields = '__all__'