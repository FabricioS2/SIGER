from django.shortcuts import render

from django.http import HttpResponse


def confirmar_refeicao(request):
   valor = 3
   return render(request, 'Confirmar_refeicao/index.html',{'valor': valor})

