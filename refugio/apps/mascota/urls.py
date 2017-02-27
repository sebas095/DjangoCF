from django.conf.urls import url
from .views import index, MascotaCreate, mascota_edit, mascota_delete, MascotaList

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo/$', MascotaCreate.as_view(), name='mascota_crear'),
    url(r'^listar/$', MascotaList.as_view(), name='mascota_list'),
    url(r'^editar/(?P<id_mascota>\d+)/$', mascota_edit, name='mascota_editar'),
    url(r'^eliminar/(?P<id_mascota>\d+)/$', mascota_delete, name='mascota_eliminar'),
]