from django.urls import path
from escritorio.views import *

urlpatterns = [
    path('faturas/', faturas.as_view(), name="faturas"),
    path('selecionarUmaFatura/', selecionarUmaFatura, name="selecionarUmaFatura"),
    path('selecionarUmaFaturaPorId/', selecionarUmaFaturaPorId, name="selecionarUmaFaturaPorId"),
    path('selecionarParaEditarFatura/', selecionarParaEditarFatura, name='selecionarParaEditarFatura'),
    path('criarFatura/', criarFatura, name="criarFatura"),
    path('recibos/', recibos.as_view(), name="recibos"),
    path('selecionarUmRecigo/', selecionarUmRecigo, name="selecionarUmRecigo"),
    path('pagarFatura/', pagarFatura, name="pagarFatura"),
    path('selecionarPagsDever/', selecionarPagsDever, name="selecionarPagsDever"),    
]
