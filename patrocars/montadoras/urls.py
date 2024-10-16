from django.urls import path
from .views import MontadoraView

urlpatterns = [
    path('',MontadoraView.list_all),
    path('criar/',MontadoraView.create),
    path('save/',MontadoraView.save,name='montadora_save')
    
]
