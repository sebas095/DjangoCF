from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from .forms import RegistroForm, User

# Create your views here
class RegistroUsuario(CreateView):
    model = User
    template_name = 'usuario/registrar.html'
    form_class = RegistroForm
    success_url = reverse_lazy('mascota_list')
