# Code modified from mini project

from django import forms
from .models import Product, Department


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        departments = Department.objects.all()
        friendly_names = [(d.id, d.get_friendly_name()) for d in departments]

        self.fields['department'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
    

    

