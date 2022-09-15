from multiprocessing import context
from operator import mod
from urllib import request
from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,ListView,DeleteView,UpdateView
from .models import Perfil
from django.urls import reverse_lazy

class PerfilView(TemplateView):
    template_name = 'perfil.html'

class PerfilList(ListView):
    template_name = 'list.html'
    model = Perfil
    fields = '__all__'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['list'] = Perfil.objects.all()
        return context




class PerfilCreate(CreateView):
    template_name = 'create.html'
    model = Perfil
    fields = '__all__'
    success_url = '.'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['Perfil'] = Perfil.objects.all()
        return context



class PerfilDelete(DeleteView):
    template_name = 'delete.html'
    model = Perfil
    fields = '__all__'
    success_url = reverse_lazy ('list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['Perfil'] = Perfil.objects.all()
        return context


class PerfilUpdate(UpdateView):
    template_name = 'update.html'
    model = Perfil
    success_url = reverse_lazy ('list')
    fields = '__all__'




















# class Perfils(ListView):
#     template_name = 'perfils.html'
#     model = Perfil
#     fields = '__all__'
#     queryset = Perfil.objects.all()
#     # def get_context_data(self, **kwargs):
#     #     context = super().get_context_data(**kwargs)
#     #     context ['list'] = Perfil.objects.all()
#     #     return context

