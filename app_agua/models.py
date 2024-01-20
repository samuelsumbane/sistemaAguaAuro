from django.db import models
from django.views.generic import ListView
from django.contrib.auth import get_user_model
User = get_user_model()


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    codigo_cliente = models.IntegerField(unique=True)
    nome_cliente = models.CharField(max_length=255)
    telefone_cliente = models.CharField(max_length=40)
    endereco_cliente = models.CharField(max_length=40)
    is_active = models.BooleanField(null=True)
    created_at = models.CharField(max_length=15, null=True)

    def __str__(self):
        return self.nome_cliente



class Definicao(models.Model):
    def_id = models.AutoField(primary_key=True)
    def_consumomin = models.IntegerField()
    def_metrocubico = models.FloatField()
    def_taxafixa = models.FloatField()
    def_iva = models.IntegerField()
    def_vencimentoday = models.CharField(max_length=40)
    def_multaforadoprazo = models.FloatField()
    multar = models.BooleanField()

    def __str__(self):
        return self.def_id


class Atividade(models.Model):
    act_id = models.AutoField(primary_key=True)
    acao = models.CharField(max_length=20)
    valor = models.CharField(max_length=30)
    dia = models.CharField(max_length=10)
    hora = models.CharField(max_length=10)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    vda = models.CharField(max_length=40) # validade
    doc_id = models.IntegerField(null=True)



