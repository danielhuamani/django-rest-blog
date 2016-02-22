from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AutorSerializer, PublicacionSerializer, ComentarioSerializer
from .models import Autor, Publicacion, Comentario


class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer


class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


class PublicacionViewSet(viewsets.ModelViewSet):
    queryset = Publicacion.objects.all()
    serializer_class = PublicacionSerializer
