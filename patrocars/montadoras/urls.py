from django.urls import path
from .views import MontadoraView

urlpatterns = [
    path('',MontadoraView.list_all),
    path('criar/',MontadoraView.create),
    path('post/',MontadoraView.post,name='montadora_save')
    
]
