from django.urls import path
from clientes_app.views import ListaUsuariosView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('lista_clientes/', ListaUsuariosView.as_view(), name='lista_clientes'),
]