from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponseRedirect
from .models import Montadora, MontadoraForm

class MontadoraView:
    def list_all(req):
        montadoras = Montadora.objects.all()
        return render(req,'montadoras/list_montadoras.html',context={'montadoras': montadoras})

    def create(req):
        return render(req,'montadoras/create_montadora.html')
    
    def edit(req, id):
        montadora = get_object_or_404(Montadora,id=id)
        return render(req,'montadoras/update_montadora.html',context={'montadora': montadora})
    
    def put(req: HttpRequest):
        form = MontadoraForm(req.POST)
        if form.is_valid():
            montadora = get_object_or_404(Montadora,id=form.cleaned_data['id'])
            montadora.name = form.cleaned_data['name']
            montadora.country = form.cleaned_data['country']
            montadora.foundation_year = form.cleaned_data['foundation_year']
            montadora.save()
        return HttpResponseRedirect("/montadoras")

    def post(req: HttpRequest):
        form = MontadoraForm(req.POST)
        #  if request.method == 'POST':
        if form.is_valid():
            new_montadora =  Montadora(name=form.cleaned_data['name'],country=form.cleaned_data['country'] , foundation_year=form.cleaned_data['foundation_year'])    
            new_montadora.save()
        return HttpResponseRedirect("/montadoras")