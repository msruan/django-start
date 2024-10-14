from django.shortcuts import render
from django.http import HttpResponse
from .models import Montadora

class MontadoraView:
    def list_all(req):
        montadoras = Montadora.objects.all();
        return render(req,'montadoras.html',context={'montadoras': montadoras});

    def create(req):
        montadora_fiat = Montadora(name='Fiat',country ='Itália', foundation_year=1923)
        montadora_byd = Montadora(name='BYD',country ='Japão', foundation_year=2000)
        montadora_fiat.save();
        montadora_byd.save();
        return HttpResponse('Sucessful!')