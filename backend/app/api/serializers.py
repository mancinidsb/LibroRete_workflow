from rest_framework import serializers
from .models import Usuario, Perfil

class UsuarioSerializer(serializers.ModelSerializer): 
  class Meta: 
    model = Usuario 
    fields = '__all__' # Inclui todos os campos da tabela

class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = '__all__'