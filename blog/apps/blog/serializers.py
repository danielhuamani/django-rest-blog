from rest_framework import serializers
from .models import Autor, Publicacion, Comentario


class ComentarioSerializer(serializers.ModelSerializer):
    # RelatedField(source='fk_publicacion', read_only=True)
    class Meta:
        model = Comentario
        # fields = ('coment', 'fecha', 'usuario')


class AutorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Autor
        fields = ('email', 'nombre')


class PublicacionSerializer(serializers.ModelSerializer):

    contenido_truncado = serializers.CharField(source='contenido_trunc')

    class Meta:
        model = Publicacion
        fields = ('fk_autor', 'titulo', 'slug', 'foto', 'contenido', 'fecha', 'id', 'publicacion_comentario', 'contenido_truncado')
        depth = 1
