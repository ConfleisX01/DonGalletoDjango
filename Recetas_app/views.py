from django.shortcuts import render
from . import forms
from django.urls import reverse_lazy
from django.views.generic import FormView

# Create your views here.
class crearReceta(FormView):
    template_name = 'crear_receta.html'
    form_class = forms.RecetaRegistrar
    success_url = reverse_lazy('lista_recetas')
    def form_valid(self, form):
        return super().form_valid(form)