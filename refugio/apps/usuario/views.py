from django.views.generic import CreateView
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from rest_framework.views import APIView
from .forms import RegistroForm, User
from .serializers import UserSerializer
import json

# Create your views here
class RegistroUsuario(CreateView):
    model = User
    template_name = 'usuario/registrar.html'
    form_class = RegistroForm
    success_url = reverse_lazy('mascota_list')

class UserAPI(APIView):
    serializer = UserSerializer

    def get(self, request, format=None):
        lista = User.objects.all()
        response = self.serializer(lista, many=True)
        return HttpResponse(json.dumps(response.data), content_type='application/json')