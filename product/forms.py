from django import forms
from django.forms.widgets import TextInput, Textarea, HiddenInput, Select
from django.utils.translation import gettext_lazy as _
from product.models import Category, Product


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = ['is_deleted']
        widgets = {
            'name': TextInput(attrs={'class': 'required form-control ', 'placeholder': 'Name'})
        }
        error_messages = {
            'name': {
                'required': _("Name field is required."),
            }
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['is_deleted']
        widgets = {
            'name': TextInput(attrs={'class': 'required form-control ', 'placeholder': 'Name'}),
            'price': TextInput(attrs={'class': 'required form-control ', 'placeholder': 'Price'}),
            'category': Select(attrs={'class': 'required form-control ', 'placeholder': 'Category'}),
            'description': TextInput(attrs={'class': 'required form-control ', 'placeholder': 'Description'})
        }
        error_messages = {
            'name': {
                'required': _("Name field is required."),
            },
            'price': {
                'required': _("Price field is required."),
            },
            'category': {
                'required': _("Category field is required."),
            },
            'description': {
                'required': _("Description field is required."),
            },
        }
