from django import forms
from.models import Product

class ProductForm(forms.Form):
    name = forms.CharField( max_length=200, label="Nombre")
    description = forms.CharField(label="Descripcion", max_length=300)
    price = forms.DecimalField(label="Precio", max_digits=10, decimal_places=2)
    available = forms.BooleanField(label="Disponible", initial=True, required=False)
    photo = forms.ImageField(label="Foto", required=False)


    def save(self):
        Product.objects.create(
            name = self.cleaned_data["name"],
            description = self.cleaned_data["description"],
            price = self.cleaned_data["price"],
            available = self.cleaned_data["available"],
            photo = self.cleaned_data["photo"],
        )