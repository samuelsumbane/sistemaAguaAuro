from django.db import models
from django.views.generic import ListView
from app_agua.models import *


'''
Total de Faturas Emitidas:


Mostre o número de faturas pendentes e pagas. Isso pode ser útil para avaliar a saúde financeira geral.
Valor Total de Faturas Emitidas:

Apresente o valor total acumulado de todas as faturas emitidas.
Percentual de Pagamento:

Calcule a porcentagem de faturas pagas em relação ao total.
Histórico de Pagamentos por Mês/Ano:

Forneça um gráfico ou tabela mostrando o histórico de pagamentos ao longo do tempo.
Top Clientes Inadimplentes:

Liste os clientes com as maiores dívidas em aberto.
Estatísticas de Consumo:

Se aplicável, inclua informações sobre o consumo médio, máximo e mínimo dos clientes.
Recibos Recentes:

Mostre os recibos mais recentes emitidos, destacando os pagamentos realizados.
Resumo de Dívidas por Cliente:

Apresente uma visão geral das dívidas de cada cliente.
Estimativa de Lucro/Prejuízo:

Se possível, inclua uma estimativa de lucro ou prejuízo com base nas faturas emitidas e nos pagamentos recebidos.
Evolução do Número de Clientes:

Mostre como o número de clientes tem evoluído ao longo do tempo.
Alertas ou Notificações:

Implemente alertas para faturas em atraso, pagamentos pendentes, etc.
Estatísticas de Emissão de Faturas por Período:

Apresente um gráfico mostrando a distribuição das faturas emitidas ao longo do tempo.
'''

class Fatura(models.Model):
    fat_id = models.AutoField(primary_key=True)
    fat_code = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    leituraatual = models.IntegerField()
    consumofaturado = models.IntegerField()
    fat_divida = models.IntegerField()
    fat_mes = models.CharField(max_length=20)
    fat_ano = models.CharField(max_length=4)
    fat_key = models.IntegerField()
    valordafatura = models.IntegerField()
    fat_emissao = models.CharField(max_length=15)

    class Meta:
        verbose_name = 'Fatura'
        verbose_name_plural = 'Faturas'

    def __str__(self):
        return f"Fatura {self.fat_id} - Cliente: {self.fat_code.codigo_cliente}"


class Pagamento(models.Model):
    pag_id = models.AutoField(primary_key=True)
    pag_code = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    valordafatura = models.FloatField()
    pag_totalpago = models.FloatField(null=True)
    pag_divida = models.FloatField()
    pag_mes = models.CharField(max_length=10)
    pag_ano = models.CharField(max_length=10)
    pag_key = models.IntegerField()
    pag_idgroup = models.TextField(null=True)

    def __str__(self):
        return f"Recibo {self.pag_id} - Cliente: {self.pag_code.codigo_cliente}"
