# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254, verbose_name=b'Email', blank=True)),
                ('nombre', models.CharField(max_length=20, verbose_name=b'nombre', blank=True)),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autores',
            },
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('coment', models.TextField(verbose_name=b'coment')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.CharField(max_length=25, verbose_name=b'usuario')),
            ],
            options={
                'verbose_name': 'Comentario',
                'verbose_name_plural': 'Comentarios',
            },
        ),
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=20, verbose_name=b'titulo')),
                ('slug', models.SlugField(editable=False)),
                ('foto', models.ImageField(upload_to=b'uploads/', blank=True)),
                ('contenido', models.TextField(verbose_name=b'contenido')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('fk_autor', models.ForeignKey(related_name='autor_publicacion', verbose_name=b'seleccione Autor', to='blog.Autor')),
            ],
            options={
                'verbose_name': 'Publicacion',
                'verbose_name_plural': 'Publicaciones',
            },
        ),
        migrations.AddField(
            model_name='comentario',
            name='fk_publicacion',
            field=models.ForeignKey(related_name='publicacion_comentario', verbose_name=b'selecciona Publicacion', to='blog.Publicacion'),
        ),
    ]
