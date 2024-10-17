from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Montadora, MontadoraForm
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    TemplateView,
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