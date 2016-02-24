from rest_framework import serializers
from .models import Autor, Publicacion, Comentario


class PubliSerializer(serializers.HyperlinkedModelSerializer):
    fk_publicacion = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='blog:publicacion-detail')
    class Meta:
        model = Publicacion


class PublicacionSerializer(serializers.ModelSerializer):

    contenido_truncado = serializers.CharField(source='contenido_trunc')

    class Meta:
        model = Publicacion
        fields = ('fk_autor', 'titulo', 'slug', 'foto', 'contenido','fecha', 'id', 'publicacion_comentario', 'contenido_truncado')
        depth = 1


class ComentarioSerializer(serializers.ModelSerializer):
    # RelatedField(source='fk_publicacion', read_only=True)
    # fk_publicacion = PubliSerializer()
    fecha_cort = serializers.CharField(source="fecha_corta")

    class Meta:
        model = Comentario
        fields = ('coment', 'fecha', 'fecha_cort', 'usuario', 'fk_publicacion')


class AutorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Autor
        fields = ('email', 'nombre')
