from django.conf.urls import include, url
from rest_framework import routers
from . import views
from .models import Publicacion
router = routers.DefaultRouter()
router.register(r'autores', views.AutorViewSet)
router.register(r'publicaciones', views.PublicacionViewSet)
router.register(r'comentarios', views.ComentarioViewSet)
urlpatterns = [
    # Examples:
    url(r'^autor$', views.crear_autor, name='crear_autor'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^api/', include(router.urls)),

]
