from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required

# from escritorio.models import *
from app_agua.models import *
from django.db.models import Q
# Create your views here.

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



def criarCliente(request):
    action = request.POST.get('action')
    id = request.POST.get('idInput')

    if request.method == "POST":
        cliente = ""
        if action == "create":
            cliente = Cliente()

        elif action == "update":
            cliente = Cliente.objects.get(id_cliente=id)

        vcodigo = request.POST.get('codigo')
        vnome = request.POST.get("nome")
        vtelefone = request.POST.get("telefone")
        vendereco = request.POST.get("endereco")

        cliente.codigo_cliente = vcodigo
        cliente.nome_cliente = vnome
        cliente.telefone_cliente = vtelefone
        cliente.endereco_cliente = vendereco
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
        multar = request.POST.get("multar") or "False"
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


