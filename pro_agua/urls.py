
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
    path('numeroTotal', numeroTotal, name="numeroTotal"),
    path('chartPagamento/', chartPagamento, name="chartPagamento"),
    path('definicoes/', definicao, name="definicoes"),
    path('selecionarDefinicoes/', selecionarDefinicoes, name="selecionarDefinicoes"),
    path('updateDef/', updateDef, name="updateDef"),    
    path('', include('escritorio.urls')),
    path('', include('contas.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('atividades', atividade.as_view(), name="atividades"),
    path('relatorio/', relatorio, name="relatorio"),
    path('aplicarMulta/', aplicarMulta, name="aplicarMulta")
    
]