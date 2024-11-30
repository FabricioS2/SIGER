from django.urls import path
from . import views

urlpatterns = [
   path('confirmar_refeicao', views.confirmar_refeicao, name="confirmar_refeicao")
]
