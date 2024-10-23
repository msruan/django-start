from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import requires_csrf_token
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from .models import Montadora, MontadoraForm, ModeloVeiculo, ModeloVeiculoForm, Veiculo, VeiculoForm
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    UpdateView,
)

class MontadoraView:


    @method_decorator(csrf_protect, name='dispatch')
    def create(req: HttpRequest):
        if req.method == "POST":
            form = MontadoraForm(req.POST)
            #  if request.method == 'POST':
            if form.is_valid():
                new_montadora =  Montadora(name=form.cleaned_data['name'],country=form.cleaned_data['country'] , foundation_year=form.cleaned_data['foundation_year'],avatar_url=form.cleaned_data['avatar_url'])    
                new_montadora.save()
                return HttpResponseRedirect("/montadoras")
            else:
                # Aqui você pode imprimir os erros
                print(form.errors)  # Para depuração no console
                return render(req, 'montadoras/create_montadora.html', {'form': form})  # Retornar o formulário com erros
        else: 
            return render(req,'montadoras/create_montadora.html')

    @method_decorator(csrf_protect, name='dispatch')
    def put(req: HttpRequest, pk: int):
        if req.method == "POST":
            form = MontadoraForm(req.POST)
            if form.is_valid():
                montadora = get_object_or_404(Montadora,id=pk)
                montadora.name = form.cleaned_data['name']
                montadora.country = form.cleaned_data['country']
                montadora.foundation_year = form.cleaned_data['foundation_year']
                montadora.save()
            return HttpResponseRedirect("/montadoras")
        else: 
            return render(req,'montadoras/update_montadora.html')

    class ListAll(ListView):
        model = Montadora
        template_name = "montadoras/list_montadoras.html"

    class Create(CreateView):
        model = Montadora
        form_class = MontadoraForm
        template_name = "montadoras/create_montadora.html"
        success_url = reverse_lazy("montadoras_list")

   
    class Update(UpdateView):
        model = Montadora
        form_class = MontadoraForm
        template_name = "montadoras/update_montadora.html"
        success_url = reverse_lazy("montadoras_list")
    
    class Delete(DeleteView):
        model = Montadora
        success_url = reverse_lazy('montadoras_list')  # Redirecionar após a exclusão

        def post(self, request, *args, **kwargs):
            return self.delete(request, *args, **kwargs)
        
class ModeloVeiculoView:

    class ListAll(ListView):
        model = ModeloVeiculo
        template_name = "modelos/list_modelos.html"

    class Create(CreateView):
        model = ModeloVeiculo
        form_class = ModeloVeiculoForm
        template_name = "modelos/create_modelo.html"
        success_url = reverse_lazy("modelos_list")

    class Update(UpdateView):
        model = ModeloVeiculo
        form_class = ModeloVeiculoForm
        template_name = "modelos/update_modelo.html"
        success_url = reverse_lazy("modelos_list")
    
    class Delete(DeleteView):
        model = ModeloVeiculo
        success_url = reverse_lazy('modelos_list')  # Redirecionar após a exclusão

        def post(self, request, *args, **kwargs):
            return self.delete(request, *args, **kwargs)
        
class VeiculoView:

    class ListAll(ListView):
        model = Veiculo
        template_name = "veiculos/list_veiculos.html"

    class Create(CreateView):
        model = Veiculo
        form_class = VeiculoForm
        template_name = "veiculos/create_veiculo.html"
        success_url = reverse_lazy("veiculos_list")

    class Update(UpdateView):
        model = Veiculo
        form_class = VeiculoForm
        template_name = "veiculos/update_veiculo.html"
        success_url = reverse_lazy("veiculos_list")
    
    class Delete(DeleteView):
        model = Veiculo
        success_url = reverse_lazy('veiculos_list')  # Redirecionar após a exclusão

        def post(self, request, *args, **kwargs):
            return self.delete(request, *args, **kwargs)