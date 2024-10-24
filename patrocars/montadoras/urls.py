from django.urls import path
from .views import MontadoraView, ModeloVeiculoView, VeiculoView, admin

urlpatterns = [
    path('',MontadoraView.ListAll.as_view(),name='montadoras_list'),
    path('admin/',admin,name='admin_page'),
    path('montadoras/criar/',MontadoraView.Create.as_view(),name='montadora_create'),
    path('montadoras/editar/<int:pk>/',MontadoraView.Update.as_view(),name='montadora_put'),
    path('montadoras/deletar/<int:pk>/',MontadoraView.Delete.as_view(),name='montadora_delete'),

    path('modelos/',ModeloVeiculoView.ListAll.as_view(),name='modelos_list'),
    path('modelos/criar/',ModeloVeiculoView.Create.as_view(),name='modelo_save'),
    path('modelos/editar/<int:pk>/',ModeloVeiculoView.Update.as_view(),name='modelo_put'),
    path('modelos/deletar/<int:pk>/',ModeloVeiculoView.Delete.as_view(),name='modelo_delete'),

    path('veiculos/',VeiculoView.ListAll.as_view(),name='veiculos_list'),
    path('veiculos/criar/',VeiculoView.Create.as_view(),name='veiculo_save'),
    path('veiculos/editar/<int:pk>/',VeiculoView.Update.as_view(),name='veiculo_put'),
    path('veiculos/deletar/<int:pk>/',VeiculoView.Delete.as_view(),name='veiculo_delete'),
]
