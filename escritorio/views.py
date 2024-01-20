from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from escritorio.models import *
from django.db.models import Q
from datetime import datetime
from django.core.serializers import serialize
from app_agua.views import saveAtivity


dataEHoraAtual = datetime.now()


class faturas(ListView):

    model = Fatura
    template_name = "faturas.html"

    def render_to_response(self, context, **response_kwargs):
        if self.request.GET.get("datatables"):
            draw = int(self.request.GET.get("draw", "1"))
            length = int(self.request.GET.get("length", "10"))
            start = int(self.request.GET.get("start", "0"))
            sv = self.request.GET.get("search[value]", None)
            qs = self.get_queryset().order_by("fat_id")
            if sv:
                qs = qs.filter(
                    Q(fat_code__icontains=sv)
                    | Q(fat_mes__icontains=sv)
                    | Q(fat_ano__icontains=sv)

                )
            filtered_count = qs.count()
            qs = qs[start: start + length]

            data = []
            for fat in qs:
                row_data = {
                    'fat_id': fat.fat_id,
                    'fat_code': fat.fat_code.codigo_cliente,
                    'nome_cliente':fat.fat_code.nome_cliente,
                    'leituraatual': fat.leituraatual,
                    'consumofaturado': fat.consumofaturado,
                    'fat_divida': fat.fat_divida,
                    'fat_mes': fat.fat_mes,
                    'fat_ano': fat.fat_ano,
                    'valordafatura':fat.valordafatura,
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



def selecionarUmaFatura(request):
    if request.method == 'GET':
        codigo = request.GET.get('codigo')
        mes = request.GET.get('mes')
        ano = request.GET.get('ano')
        
        meses = ('Janeiro', 'Fevereiro', 'Marco', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembr',)
        mesAtualNr = dataEHoraAtual.strftime('%m')
        mesAtualText = meses[int(mesAtualNr) - 1]
        
        try:
            data = Fatura.objects.filter(fat_code_id=codigo, fat_mes=mesAtualText, fat_ano=ano).count()
            if data > 0:
                return JsonResponse({'data': '405'}) # fatura do mesmo mes encontrada
            else:        
                try:
                    filteredFat = Fatura.objects.get(fat_code_id=codigo, fat_mes=mes, fat_ano=ano)

                    data = {'fat_id': filteredFat.fat_id, 'fat_code': filteredFat.fat_code_id,
                            'leituraatual': filteredFat.leituraatual, 'fat_divida': filteredFat.fat_divida,
                            'fat_mes': filteredFat.fat_mes, 'fat_ano': filteredFat.fat_ano}
                    return JsonResponse({'data': data})

                except ObjectDoesNotExist:
                    try:
                        data = Fatura.objects.filter(fat_code_id=codigo).count()
                        if data > 0:
                            return JsonResponse({'data': '406'}) #mes anterior nao encontrada mas ha faturas
                        else:
                            return JsonResponse({'data': '407'}) #mes anterior nao encontrada e nem tem faturas
                            
                    
                    except ObjectDoesNotExist:
                        data = "404"
                        return JsonResponse({'data': data})
    
        except ObjectDoesNotExist:            
            data = "404"
            return JsonResponse({'data': data})
        
        
        
def selecionarUmaFaturaPorId(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        try:
            filteredFat = Fatura.objects.get(fat_id=id)

            data = {'fat_id': filteredFat.fat_id, 'fat_nome':filteredFat.fat_code.nome_cliente, 'fat_bairro':filteredFat.fat_code.endereco_cliente , 'fat_code': filteredFat.fat_code_id,
                    'leituraatual': filteredFat.leituraatual, 'valordafatura':filteredFat.valordafatura, 'consumofaturado':filteredFat.consumofaturado, 'fat_divida': filteredFat.fat_divida,
                    'fat_mes': filteredFat.fat_mes, 'fat_ano': filteredFat.fat_ano}
    
            return JsonResponse({'data': data})

        except ObjectDoesNotExist:
            data = '404'
            return JsonResponse({'data': data})



def selecionarParaEditarFatura(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        try:
            filteredFat = Fatura.objects.get(fat_id=id)

            fatarray = {'fat_id':filteredFat.fat_id,'fat_code_id': filteredFat.fat_code_id, 'fat_mes': filteredFat.fat_mes, 'fat_ano': filteredFat.fat_ano, 'fat_code':filteredFat.fat_code.codigo_cliente, 'leituraatual':filteredFat.leituraatual, 'consumofaturado':filteredFat.consumofaturado, 'valordafatura':filteredFat.valordafatura}
            
            filteredPag = Pagamento.objects.filter(pag_code_id=fatarray['fat_code_id'], pag_mes=fatarray['fat_mes'], pag_ano=fatarray['fat_ano'] ).values()
            
            data = list(filteredPag)
            
            return JsonResponse({'data': data, 'dataFat':fatarray})
                    
        except ObjectDoesNotExist:
            data = '404'
            return JsonResponse({'data': data})



def selecionarPagsDever(request):
    if request.method == 'GET':
        codigo = request.GET.get('codigo')
        try:
            filtered_pagamentos = Pagamento.objects.filter(pag_code_id=codigo).values()
            data = list(filtered_pagamentos)
            return JsonResponse({'data': data})

        except ObjectDoesNotExist:
            data = '404'
            return JsonResponse({'data': data})


def criarFatura(request):
    if request.method == 'POST':
        
        ano_atual = dataEHoraAtual.strftime('%Y')
        meses = ('Janeiro', 'Fevereiro', 'Marco', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro',)
        mes = dataEHoraAtual.strftime('%m')
        mes_atual = meses[int(mes) - 1]
        fat_emissao = dataEHoraAtual.strftime('%d.%m.%Y')

        leituraatual = request.POST.get('leituraatual')
        fatcode = request.POST.get('fatCode')
        valordafatura = request.POST.get('valorFatura')
        consumofaturado = request.POST.get('consumofaturado')
        action = request.POST.get('action')
        userid = request.POST.get('userid')
        
        if action == "editarFatura":
            fatid = request.POST.get('fatid')
            pagid = request.POST.get('pagid')
            efatura = Fatura.objects.get(fat_id=fatid)
            efatura.leituraatual = leituraatual
            efatura.consumofaturado = consumofaturado
            efatura.valordafatura = valordafatura
            efatura.save()
            
            epag = Pagamento.objects.get(pag_id=pagid)
            epag.valordafatura = valordafatura
            epag.save()
 
            data = '201'
        else:    
            fatura = Fatura()    
            fatura.fat_code_id = fatcode
            fatura.leituraatual = leituraatual
            fatura.consumofaturado = consumofaturado
            fatura.fat_divida = 0
            fatura.fat_mes = mes_atual
            fatura.fat_ano = ano_atual
            fatura.fat_key = 1
            fatura.valordafatura = valordafatura
            fatura.fat_emissao = fat_emissao
            fatura.save()

            saveAtivity("F. Criada", valordafatura, userid, 'infinity')
            
            # criar minRecibo
            pag = Pagamento()
            pag.pag_code_id = fatcode
            pag.valordafatura = valordafatura
            pag.pag_totalpago = 0
            pag.pag_divida = 0
            pag.pag_mes = mes_atual
            pag.pag_ano = ano_atual
            pag.pag_key = 1
            # pag_idgroup =  
            pag.save()

            data = '200'
        return JsonResponse({'data': data})




class recibos(ListView):

    model = Pagamento
    template_name = "recibos.html"

    def render_to_response(self, context, **response_kwargs):
        if self.request.GET.get("datatables"):
            draw = int(self.request.GET.get("draw", "1"))
            length = int(self.request.GET.get("length", "10"))
            start = int(self.request.GET.get("start", "0"))
            sv = self.request.GET.get("search[value]", None)
            qs = self.get_queryset().order_by("pag_id")
            if sv:
                qs = qs.filter(
                    Q(fat_code__icontains=sv)
                    | Q(fat_mes__icontains=sv)
                    | Q(fat_ano__icontains=sv)
                )
            filtered_count = qs.count()
            qs = qs[start: start + length]

            data = []
            for pag in qs:
                row_data = {
                    'pag_id': pag.pag_id,
                    'pag_code': pag.pag_code.codigo_cliente,
                    'nome_cliente':pag.pag_code.nome_cliente,
                    'valordafatura': pag.valordafatura,
                    'pag_totalpago': pag.pag_totalpago,
                    'pag_divida': pag.pag_divida,
                    'pag_mes': pag.pag_mes,
                    'pag_ano': pag.pag_ano,
                    'pag_idgroup': pag.pag_idgroup,
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



def selecionarUmRecigo(request):
    pass


def retornaridgroup():
    idgroup = dataEHoraAtual.strftime('%d%m%H%M%S')
    return idgroup

def pagarFatura(request):
         
    if request.method == "POST":
        divlen = request.POST.get('divsLen')
        userid = request.POST.get('userid')
        idgroup = request.POST.get('idgroupinput')

               
        for i in range(int(divlen)):
            valordafatura = request.POST.get(f"valorapagar{i}")
            divida = request.POST.get(f'dividaapagar{i}')
            id = request.POST.get(f'pagid{i}')
            mespag = request.POST.get(f'mes{i}')
            anopag = request.POST.get(f'ano{i}')    
                
            pagamento = Pagamento.objects.get(pag_code_id=id, pag_mes=mespag, pag_ano=anopag)
            
            if valordafatura != "" or divida != "":
                if float(pagamento.valordafatura) < float(valordafatura) or float(pagamento.pag_divida) < float(divida):
                    data = "203"
                else:
                    if pagamento.pag_totalpago != "":
                        pagamento.pag_totalpago += float(valordafatura)
                    else:
                        pagamento.pag_totalpago = float(valordafatura)
                           
                    pagamento.pag_divida -= float(divida)
                    pagamento.pag_idgroup = idgroup
                    pagamento.save()
                    saveAtivity("F. Paga", valordafatura, userid, 'infinity', id)
                    data = "200"
                         
        return JsonResponse({'data': data})
                     
        
def pagPorIdGroup(request):
    idgroup = request.GET['idgroup']
    pags = Pagamento.objects.filter(pag_idgroup=idgroup).values()
    data = list(pags)
    dataCliente = list(Cliente.objects.filter(id_cliente=pags[0]['pag_code_id']).values())
    return JsonResponse({'data':data, 'dataCliente':dataCliente})


