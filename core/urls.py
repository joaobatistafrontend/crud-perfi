from django.views.generic import TemplateView
from django.urls import path
from core import views

urlpatterns = [
    path('',views.PerfilView.as_view(), name='index'),
    path('create/',views.PerfilCreate.as_view(), name='create'),
    path('list/',views.PerfilList.as_view(), name='list'),
    path('delete/<int:pk>/',views.PerfilDelete.as_view(), name='delete'),
    path('update/<int:pk>/',views.PerfilUpdate.as_view(), name='update'),
]

