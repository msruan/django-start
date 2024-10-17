from django.urls import path
from .views import MontadoraView

urlpatterns = [
    path('',MontadoraView.ListAll.as_view(),name='montadoras_list'),
    path('criar/',MontadoraView.Create.as_view(),name='montadora_save'),
    path('editar/<int:pk>/',MontadoraView.Update.as_view()),
    path('deletar/<int:pk>/',MontadoraView.Delete.as_view(),name='montadora_delete'),
]
