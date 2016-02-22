from django.db import models
from django.template.defaultfilters import slugify


class Autor(models.Model):
    nombre = models.CharField('nombre', blank=True, max_length=20)
    foto_perfil = models.ImageField(upload_to='uploads/', default='pic_folder/None/no-img.jpg')
    slug = models.SlugField(editable=False)
    biografia = models.TextField('biografia')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = u'Autor'
        verbose_name_plural = u'Autores'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super(Autor, self).save(*args, **kwargs)


class Publicacion(models.Model):
    fk_autor = models.ForeignKey(Autor, related_name='autor_publicacion', verbose_name='seleccione Autor')
    titulo = models.CharField('titulo', max_length=20)
    slug = models.SlugField(editable=False)
    foto = models.ImageField(upload_to='uploads/', default='pic_folder/None/no-img.jpg', blank=True)
    contenido = models.TextField('contenido')
    fecha = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = u'Publicacion'
        verbose_name_plural = u'Publicaciones'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo)
        super(Publicacion, self).save(*args, **kwargs)


class Comentario(models.Model):
    fk_publicacion = models.ForeignKey(Publicacion, related_name='publicacion_comentario', verbose_name='selecciona Publicacion')
    coment = models.TextField('coment')
    fecha = models.DateTimeField(auto_now=True)
    usuario = models.CharField('usuario', max_length=25)

    def __str__(self):
        return self.usuario

    class Meta:
        verbose_name = u'Comentario'
        verbose_name_plural = u'Comentarios'
