from django.db import models
from django.views.generic import ListView
from app_agua.models import *


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
