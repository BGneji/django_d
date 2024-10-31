from django import forms
from .models import Product
from django.utils.text import slugify

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'slug', 'price', 'category']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'name': "search1"}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control', 'name': "category"}),
        }


class ProductDeleteForm(forms.Form):
    confirm = forms.BooleanField(
        required=True,
        label="Я подтверждаю удаление этого продукта.",
        widget=forms.CheckboxInput(attrs={'class': 'form-control'})
    )