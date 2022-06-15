from .models import Laptop
from django import forms

ram = [('4gb','4GB'),('8gb','8GB'),('12gb','12GB'),('16gb','16GB')]
class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = '__all__'

        labels = {
            'laptop_id':'Laptop ID',
             'name':'NAME',
             'brand':'BRAND',
             'ram':'RAM',
             'rom': 'ROM',
             'HDD':'HDD',
             'SSD':'SSD',
             'price':'PRICE'
        }

        widgets = {
            'lapto_id': forms.NumberInput(attrs={'placeholder':'Eg: 101'}),
            'name':forms.TextInput(attrs={'placeholder':'Eg: xyz'}),
            'ram': forms.RadioSelect(choices=ram),
            'rom': forms.TextInput(attrs={'placeholder':'Eg: 1TB'}),
            'HDD':forms.TextInput(attrs={'placeholder':'Eg: 512GB'}),
            'SSD': forms.TextInput(attrs={'placeholder':'Eg: 256GB'}),
            'price': forms.TextInput(attrs={'placeholder':'Eg: 75000'})
        }