from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def Login(request):
   return render(request, 'Login_Cadastro/login.html')

def Cadastro_aluno(request):
   return render(request, 'Login_Cadastro/Cadastro_aluno.html')


def Cadastro_admistrador(request):
   return render(request, 'Login_Cadastro/Cadastro_admistrador.html')


