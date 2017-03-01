from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import MascotaIndex, MascotaCreate, MascotaUpdate, MascotaDelete, MascotaList, listadousuarios

urlpatterns = [
    url(r'^$', MascotaIndex.as_view(), name='mascota_index'),
    url(r'^nuevo/$', login_required(MascotaCreate.as_view()), name='mascota_crear'),
    url(r'^listar', login_required(MascotaList.as_view()), name='mascota_list'),
    url(r'^editar/(?P<pk>\d+)/$', login_required(MascotaUpdate.as_view()), name='mascota_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$', login_required(MascotaDelete.as_view()), name='mascota_eliminar'),
    url(r'^listado', listadousuarios, name='listado'),
]