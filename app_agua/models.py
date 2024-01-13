from django.db import models
from django.views.generic import ListView


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    codigo_cliente = models.IntegerField(unique=True)
    nome_cliente = models.CharField(max_length=255)
    telefone_cliente = models.CharField(max_length=40)
    endereco_cliente = models.CharField(max_length=40)

    def __str__(self):
        return self.nome_cliente


class Usuario(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=255, default="null")
    user_username = models.CharField(max_length=40, default="null")
    user_pass = models.CharField(max_length=10, default="null")
    user_nivel = models. CharField(max_length=10, default="null")
    user_key = models.IntegerField(default="1")
    user_status = models.CharField(max_length=10, default="null")


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
    valor = models.FloatField()
    dia = models.CharField(max_length=10)
    hora = models.CharField(max_length=10)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    # don't remember vda
    vda = models.CharField(max_length=40)
    doc_id = models.IntegerField()



