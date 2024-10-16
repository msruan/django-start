from django.shortcuts import render
from django.http import HttpRequest
from .models import Montadora, MontadoraForm

class MontadoraView:
    def list_all(req):
        montadoras = Montadora.objects.all();
        return render(req,'montadoras.html',context={'montadoras': montadoras});

    def create(req):
        return render(req,'montadoras_form.html');

    def save(req: HttpRequest):
        form = MontadoraForm(req.POST)
        if form.is_valid():
            new_montadora =  Montadora(name=form.cleaned_data['name'],country=form.cleaned_data['country'] , foundation_year=form.cleaned_data['foundation_year'])    
            new_montadora.save();
        return render(req,'montadoras_form.html');