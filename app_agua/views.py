from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from datetime import datetime, date 
from escritorio.models import *
from app_agua.models import *
from django.db.models import Q
dataEHoraAtual = datetime.now()
from pro_agua.functions import *
from django.contrib.auth import get_user_model
User = get_user_model()
from django.db.models import F

def home(request):
    return render(request, 'index.html')

class clientes(ListView):

    model = Cliente
    template_name = "clientes.html"

    # @login_required(login_url='/contas/templates/login.html')
    def render_to_response(self, context, **response_kwargs):
        if self.request.GET.get("datatables"):
            draw = int(self.request.GET.get("draw", "1"))
            length = int(self.request.GET.get("length", "10"))
            start = int(self.request.GET.get("start", "0"))
            sv = self.request.GET.get("search[value]", None)
            qs = self.get_queryset().order_by("nome_cliente")
            if sv:
                qs = qs.filter(
                    Q(codigo_cliente__icontains=sv)
                    | Q(nome_cliente__icontains=sv)
                    | Q(telefone_cliente__icontains=sv)
                    | Q(endereco_cliente__icontains=sv)
                )
            filtered_count = qs.count()
            qs = qs[start: start + length]

            data = []
            for cliente in qs:
                row_data = {
                    'id_cliente': cliente.id_cliente,
                    'codigo_cliente': cliente.codigo_cliente,
                    'nome_cliente': cliente.nome_cliente,
                    'telefone_cliente': cliente.telefone_cliente,
                    'endereco_cliente': cliente.endereco_cliente,
                    'acoes': None,  # Não é necessário enviar dados específicos aqui
                }
                data.append(row_data)

            return JsonResponse(
                {
                    "recordsTotal": self.get_queryset().count(),
                    "recordsFiltered": filtered_count,
                    "draw": draw,
                    "data": data,
                },
                safe=False,
            )
        return super().render_to_response(context, **response_kwargs)


def saveAtivity(acao, valor, userid, validadeValue='clientes', docid=0):
    diaHoje = dataEHoraAtual.strftime('%d.%m.%Y')
    ativi = Atividade()
    ativi.acao = acao 
    ativi.valor = valor
    ativi.dia = diaHoje
    ativi.hora = retornarHora()
    usuario = User.objects.get(id=userid)
    ativi.usuario = usuario
    ativi.vda = retornarValidade(validadeValue)
    ativi.doc_id = docid
    ativi.save()


def criarCliente(request):
    action = request.POST.get('action')
    id = request.POST.get('idInput')
    diaHoje = dataEHoraAtual.strftime('%d.%m.%Y')
    
    if request.method == "POST":
        cliente = ""
        if action == "create":
            cliente = Cliente()
            cliente.created_at = diaHoje
            cliente.is_active = True
            
        elif action == "update":
            cliente = Cliente.objects.get(id_cliente=id)

        vcodigo = request.POST.get('codigo')
        vnome = request.POST.get("nome")
        vtelefone = request.POST.get("telefone")
        vendereco = request.POST.get("endereco")
        userid = request.POST.get('userid')

        cliente.codigo_cliente = vcodigo
        cliente.nome_cliente = vnome
        cliente.telefone_cliente = vtelefone
        cliente.endereco_cliente = vendereco
        diaHoje = dataEHoraAtual.strftime('%d.%m.%Y')
        # atividade
        saveAtivity('C. Cliente', vnome, userid, 'clientes', 0)        
        cliente.save()
        data = "success"

        return JsonResponse({'data': data})


def selecionarCliente(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        filteredCliente = Cliente.objects.get(id_cliente=id)
        data = {'id_cliente': filteredCliente.id_cliente, 'codigo_cliente': filteredCliente.codigo_cliente,
            'nome_cliente': filteredCliente.nome_cliente, 'telefone_cliente': filteredCliente.telefone_cliente,
            'endereco_cliente': filteredCliente.endereco_cliente}

        return JsonResponse({'data': data})

def selecionarTodosClientes(request):

    if request.method == 'GET':

        clientes = Cliente.objects.all()
        data = [{'id_cliente': cliente.id_cliente, 'codigo_cliente': cliente.codigo_cliente, 'nome_cliente': cliente.nome_cliente, 'telefone_cliente': cliente.telefone_cliente, 'endereco_cliente': cliente.endereco_cliente} for cliente in clientes]

        return JsonResponse({'data': data})


def editarCliente(request, id):
    vnome= request.POST.get("nome")
    vtelefone= request.POST.get("telefone")
    vendereco= request.POST.get("endereco")
    cliente = Cliente.objects.get(id_cliente=id)
    cliente.nome_cliente = vnome
    cliente.telefone_cliente = vtelefone
    cliente.endereco_cliente = vendereco
    cliente.save()
    return redirect(clientes)


def deletarCliente(request, id):
    cliente = Cliente.objects.get(id_cliente=id)
    cliente.delete()
    return redirect(clientes)


def definicao(request):
    definicoes = Definicao.objects.all()
    return render(request, "definicoes.html", {"definicoes": definicoes})

def selecionarDefinicoes(request):
    if request.method == 'GET':
        definicoes = Definicao.objects.all()
        data = [{'def_consumomin': df.def_consumomin, 'def_metrocubico': df.def_metrocubico, 'def_taxafixa': df.def_taxafixa, 'multar': df.multar, 'def_multaforadoprazo': df.def_multaforadoprazo, 'def_vencimentoday': df.def_vencimentoday, 'def_iva': df.def_iva} for df in definicoes]

        return JsonResponse({'data': data})


# pode-se melhorar isto mais tarde ~

def updateDef(request):
    if request.method == "POST":
        metrocubico = request.POST.get("metrocubico")
        taxafixa = request.POST.get("taxafixa")
        iva = request.POST.get("iva")
        vencimento = request.POST.get("vencimentoday")
        multa = request.POST.get("multaforadoprazo")
        multar = request.POST.get("multar")
        if multar == 'on':
            multar = "True"
        else: 
            multar = "False"
        consumomin = request.POST.get('consumomin')

        try:
            definicao = Definicao.objects.get(def_id=1)
            definicao.def_metrocubico = metrocubico
            definicao.def_taxafixa = taxafixa
            definicao.def_iva = iva
            definicao.def_vencimentoday = vencimento
            definicao.def_multaforadoprazo = multa
            definicao.multar = multar
            definicao.def_consumomin = consumomin
            definicao.save()
            response = '201'
            return JsonResponse({'data': response})

        except ObjectDoesNotExist:

            definica = Definicao()
            definica.def_id = 1
            definica.def_metrocubico = metrocubico
            definica.def_taxafixa = taxafixa
            definica.def_iva = iva
            definica.def_vencimentoday = vencimento
            definica.def_multaforadoprazo = multa
            definica.multar = multar
            definica.def_consumomin = consumomin

            definica.save()

            response = '200'
            return JsonResponse({'data': response})


class atividade(ListView):
    model = Atividade
    template_name = "atividades.html"

    def render_to_response(self, context, **response_kwargs):
        if self.request.GET.get("datatables"):
            draw = int(self.request.GET.get("draw", "1"))
            length = int(self.request.GET.get("length", "10"))
            start = int(self.request.GET.get("start", "0"))
            sv = self.request.GET.get("search[value]", None)
            qs = self.get_queryset().order_by("act_id")
            if sv:
                qs = qs.filter(
                    Q(acao__icontains=sv)
                    | Q(valor__icontains=sv)
                    | Q(dia__icontains=sv)
                )
            filtered_count = qs.count()
            qs = qs[start: start + length]

            data = []
            for ativi in qs:
                row_data = {
                    'act_id': ativi.act_id,
                    'acao': ativi.acao,
                    'valor': ativi.valor,
                    'dia': ativi.dia,
                    'hora': ativi.hora,
                    'usuario': ativi.usuario.first_name
                }
                data.append(row_data)

            return JsonResponse(
                {
                    "recordsTotal": self.get_queryset().count(),
                    "recordsFiltered": filtered_count,
                    "draw": draw,
                    "data": data,
                },
                safe=False,
            )
        return super().render_to_response(context, **response_kwargs)



def relatorio(request):
    id = request.POST['userid']
    usuario = User.objects.filter(id=id).values()
    
    idate_str = request.POST['initialdate']
    fdate_str = request.POST['finaldate']

    idate = datetime.strptime(idate_str, '%Y-%m-%d').date()
    fdate = datetime.strptime(fdate_str, '%Y-%m-%d').date()

    idate_str_formatted = idate.strftime('%d.%m.%Y')
    fdate_str_formatted = fdate.strftime('%d.%m.%Y')

    rel = Atividade.objects.filter(usuario_id=id, dia__range=(idate_str_formatted, fdate_str_formatted)).values()
    data = list(rel)
    return JsonResponse({'data': data, 'user':list(usuario)})


def numeroTotal(request):
    clientLen = Cliente.objects.filter().count()
    clientLenActive = Cliente.objects.filter(is_active='True').count()
    
    userLen = User.objects.filter().count()
    userLenActive = User.objects.filter(is_active='True').count()
    
    faturasEmitidas = Fatura.objects.filter().count()
    
    valorAcomulado = Fatura.objects.filter().values()
    vA = 0
    for v in valorAcomulado:
        vA += v['valordafatura']
    
    faturasPagas = Pagamento.objects.filter(pag_totalpago=F('valordafatura')).count()
        
    return JsonResponse({'clientLen':clientLen, 'clientLenActive':clientLenActive, 'userLen':userLen, 'userLenActive':userLenActive, 'faturasEmitidas':faturasEmitidas, 'valorAcomulado':vA, 'faturasPagas':faturasPagas})

    
    