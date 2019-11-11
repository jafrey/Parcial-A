from django.contrib.auth.models import User, Group
from rest_framework import serializers

#Importo los modelos para poder serializarlos

from models import cancion


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class CancionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = cancion
        fields = ['nom_cancion', 'desc_cancion', 'anio_salida']
