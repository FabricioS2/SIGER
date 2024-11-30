from django.urls import path
from . import views

urlpatterns = [
   path('', views.Login, name="Login"),
   path('Cadastro_aluno', views.Cadastro_aluno, name="Cadastro_aluno"),
   path('Cadastro_admistrador', views.Cadastro_admistrador, name="Cadastro_admistrador"),
]
