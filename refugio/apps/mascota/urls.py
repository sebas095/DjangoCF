from django.conf.urls import url
from .views import index, MascotaCreate, MascotaUpdate, MascotaDelete, MascotaList

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo/$', MascotaCreate.as_view(), name='mascota_crear'),
    url(r'^listar/$', MascotaList.as_view(), name='mascota_list'),
    url(r'^editar/(?P<pk>\d+)/$', MascotaUpdate.as_view(), name='mascota_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$', MascotaDelete.as_view(), name='mascota_eliminar'),
]