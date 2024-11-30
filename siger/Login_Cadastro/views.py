from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def Login(request):
   return render(request, 'Login_Cadastro/login.html')


