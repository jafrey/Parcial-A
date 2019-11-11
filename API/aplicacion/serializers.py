from django.contrib.auth.models import User, Group
from rest_framework import serializers

#deshabilitar la seguridad, por ahora
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


#Importo los modelos para poder serializarlos

from models import cancion, usuario


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class CancionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = cancion
        fields = ['nom_cancion', 'desc_cancion', 'anio_salida']

#@csrf_exempt
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = usuario
        fields = ['id', 'nom_usuario', 'contrasenia']
