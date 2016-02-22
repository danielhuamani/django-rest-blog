from rest_framework import serializers
from .models import Autor, Publicacion, Comentario


class ComentarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comentario
        # fields = ('coment', 'fecha', 'usuario')


class AutorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Autor
        fields = ('email', 'nombre')


class PublicacionSerializer(serializers.ModelSerializer):
    # publicacion_comentario = ComentarioSerializer(many=True)

    # autor_publicacion = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='blog:autor-detail')
    class Meta:
        model = Publicacion
        fields = ('fk_autor', 'titulo', 'slug', 'foto', 'contenido', 'fecha', 'id', 'publicacion_comentario',)
        depth = 1
