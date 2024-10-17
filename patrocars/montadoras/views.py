from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Montadora, MontadoraForm, ModeloVeiculo, ModeloVeiculoForm, Veiculo, VeiculoForm
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    UpdateView,
)

class MontadoraView:

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