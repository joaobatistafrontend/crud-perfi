from pyexpat import model
from tabnanny import verbose
from django.db import models

class Perfil(models.Model):
    nome = models.CharField(max_length=120)
    sobrenome = models.CharField(max_length=120)
    cpf = models.IntegerField()
    email = models.EmailField(max_length=120,blank=True,null=True)
    bairro = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    complemento = models.CharField(max_length=200)


    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfils'