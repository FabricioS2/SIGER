from django.urls import path
from . import views

urlpatterns = [
   path('minhas_refeicao', views.minhas_refeicao, name="minhas_refeicao")
]
