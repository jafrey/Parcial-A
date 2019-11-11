from django.shortcuts import render, render_to_response

# Create your views here.

#importa los usuarios y grupos nativos de django
from django.contrib.auth.models import User, Group

#importa las viewsets de rest_framework
from rest_framework import viewsets
from rest_framework.response import Response

#importa los serializadores que se encuentran en aplicacion/serializers.py
from aplicacion.serializers import UserSerializer, GroupSerializer, CancionSerializer, UsuarioSerializer

#importa los modelos creados en models.py
from models import cancion, usuario

#Imports para usar json y urllib
import json
import urllib
import requests

#este es para que no atomice la seguridad
from django.views.decorators.csrf import csrf_exempt


#Creacion de viewsets


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    serializer_class = GroupSerializer
    queryset = Group.objects.all()

class CancionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows canciones to be viewed or edited.
    """

    queryset = cancion.objects.all()
    serializer_class = CancionSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows canciones to be viewed or edited.
    """

    queryset = usuario.objects.all()
    serializer_class = UsuarioSerializer



## VIEW DE LOGIN

# @csrf_exempt #Para que no joda la seguridad

def login(request):

    if request.method == "GET":

    	return render_to_response('login.html')

    else:

     usuario = request.POST['usuario']
     password = request.POST['pass']
     url = 'http://127.0.0.1:8001/api-root-usuario/'
     data = urllib.urlopen(url)
     jsonData = json.loads(data)

     return render_to_response('templates/principal.html', { 'usuarios' : jsonData[results] })


#		if jsonData[0]["code"] == "200":
#
#			return render_to_response("principal.html",{ 'mensaje' : 'ok'})
#		else:
#			return render_to_response("principal.html",{ 'mensaje' : 'usuario invalido'})
