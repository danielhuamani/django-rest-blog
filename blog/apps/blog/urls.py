from django.conf.urls import include, url
from rest_framework import routers
from . import views
from .models import Publicacion
router = routers.DefaultRouter()
router.register(r'autores', views.AutorViewSet)
router.register(r'publicaciones', views.PublicacionViewSet, base_name=Publicacion)
router.register(r'comentarios', views.ComentarioViewSet)
urlpatterns = [
    # Examples:
    # url(r'^$', 'django_backbone.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^api/', include(router.urls)),
]
