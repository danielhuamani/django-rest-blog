from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
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


@csrf_exempt
def crear_autor(request):
    data = {
        "status": "error"
        }
    if request.method == "POST":
        email = request.POST.get("email")
        nombre = request.POST.get("nombre")
        titulo = request.POST.get("titulo")
        contenido = request.POST.get("contenido")
        foto = request.FILES.get("foto")
        autor = Autor(email=email, nombre=nombre)
        autor.save()
        publicacion = Publicacion(fk_autor=autor, titulo=titulo, contenido=contenido, foto=foto).save()
        data['status'] = "ok"

    return HttpResponse(json.dumps(data), content_type="application/json")
    # def list(self, request):
    #     queryset = Publicacion.objects.all()
    #     serializer = PublicacionSerializer(queryset , many=True)
    #     return Response(serializer.data)

    # def retrieve(self, request, pk=None):
    #     publicacion = get_object_or_404(Publicacion, pk=pk)
    #     serializer = PublicacionSerializer(publicacion)
    #     print "........."
    #     print serializer.data['publicacion_comentario']
    #     print "........."
    #     return Response(serializer.data['publicacion_comentario'])

    # def create(self, request):
    #     Publicacion.objects.create(fk_publicacion = request.
