from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User

class ListaUsuariosView(TemplateView):
    template_name = 'lista_clientes.html'

    def get_context_data(self):
        lista = User.objects.all()
        return {'lista': lista}