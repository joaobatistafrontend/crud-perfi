from django.contrib import admin
from .models import Perfil

@admin.register(Perfil)
class PerfilAdm(admin.ModelAdmin):
    list_display = ('nome','sobrenome','cpf','email','bairro','endereco','complemento')