from django import forms
from .models import Recetas, InsumoTemporal,IngredienteReceta


class RecetaRegistrar(forms.ModelForm):
    ingredientes = forms.ModelMultipleChoiceField(
        queryset=InsumoTemporal.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label="Ingredientes"
        
    )
    
    class Meta:
            model = Recetas
            fields = ['NombreReceta', 'cantidad_galletas', 'ingredientes']
            widgets = {
                "NombreReceta": forms.TextInput(attrs={"class": "form-control"}),
                "cantidad_galletas": forms.NumberInput(attrs={"class": "form-control"}),
                "ingredientes": forms.Select(attrs={"classs": "form-control"}),
            }
    def save(self):
        receta = Recetas(
        NombreReceta = self.cleaned_data["NombreReceta"],
        cantidad_galletas = self.changed_data["cantidad_galletas"]        
        )
        receta.save()
        receta.ingredientes.set(self.cleaned_data["ingredientes"])
        receta.save()
