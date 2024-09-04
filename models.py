from django.db import models

# Create your models here.

class Empresas(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    nome = models.CharField(max_length=64, unique=True, blank=True, null=True)
    email = models.EmailField()
    senha = models.CharField(max_length=20)
    jogo = models.CharField(max_length=30, blank=True, null=True)
    desc = models.CharField(max_length=30)

class jogo(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    empresa = models.ForeignKey(Empresas, on_delete=models.CASCADE, related_name='+')
    nome = models.CharField(max_length=64, unique=True)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    desc = models.CharField(max_length=100)
    data_lancamento = models.DateField(blank=True, null=True)

class usuario(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    nome = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=20)

class biblioteca(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    id_jogo = models.ForeignKey(jogo, on_delete=models.CASCADE)
    id_user = models.ForeignKey(usuario, on_delete= models.CASCADE)
