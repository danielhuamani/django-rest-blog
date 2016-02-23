from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import AutorSerializer, PublicacionSerializer, ComentarioSerializer
from .models import Autor, Publicacion, Comentario


class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer


class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


class PublicacionViewSet(viewsets.ViewSet):
    # queryset = Publicacion.objects.all()
    # serializer_class = PublicacionSerializer
    def list(self, request):
        queryset = Publicacion.objects.all()
        serializer = PublicacionSerializer(queryset , many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        publicacion = get_object_or_404(Publicacion, pk=pk)
        serializer = PublicacionSerializer(publicacion)
        return Response(serializer.data['publicacion_comentario'])
