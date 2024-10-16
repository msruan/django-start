from django.db import models
from django.forms import ModelForm

# Create your models here.

class Montadora(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=200)
  country = models.CharField(max_length=100)
  foundation_year = models.IntegerField()

   # Metadados
  class Meta:
        ordering = ['name','foundation_year']
  # Métodos
  def __str__(self):
  # """ String para representar o objeto MyModelName (no site Admin)."""
    return self.name

class MontadoraForm(ModelForm):
    class Meta:
        model = Montadora
        fields = ["name", "country", "foundation_year"]