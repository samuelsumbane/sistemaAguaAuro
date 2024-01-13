
from django.contrib import admin
from django.urls import path, include
from app_agua.views import *
from escritorio.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('index/', home, name="home"),
    path('clientes/', clientes.as_view(), name="clientes"),
    path('criarCliente/', criarCliente, name="criarCliente"),
    path('selecionarTodosClientes/', selecionarTodosClientes, name="selecionarTodosClientes"),
    path('selecionarCliente/', selecionarCliente, name="selecionarCliente"),
    path('faturas/', faturas.as_view(), name="faturas"),
    path('selecionarUmaFatura/', selecionarUmaFatura, name="selecionarUmaFatura"),
    path('selecionarUmaFaturaPorId/', selecionarUmaFaturaPorId, name="selecionarUmaFaturaPorId"),
    path('selecionarParaEditarFatura/', selecionarParaEditarFatura, name='selecionarParaEditarFatura'),
    path('definicoes/', definicao, name="definicoes"),
    path('selecionarDefinicoes/', selecionarDefinicoes, name="selecionarDefinicoes"),
    path('updateDef/', updateDef, name="updateDef"),
    path('criarFatura/', criarFatura, name="criarFatura"),
    path('recibos/', recibos.as_view(), name="recibos"),
    path('selecionarUmRecigo/', selecionarUmRecigo, name="selecionarUmRecigo"),
    path('pagarFatura/', pagarFatura, name="pagarFatura"),
    path('selecionarPagsDever/', selecionarPagsDever, name="selecionarPagsDever"),
    path('', include('contas.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]