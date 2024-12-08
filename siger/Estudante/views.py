from django.shortcuts import render

from django.http import HttpResponse


def minhas_refeicao(request):
   return render(request, 'Estudante/Minhas_Refeicoes.html')

