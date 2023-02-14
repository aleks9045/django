from .models import Information
from django.forms import ModelForm, TextInput


class InformationForm(ModelForm):
    class Meta:
        model = Information
        fields = ['name', 'name2', 'age', 'sex']
        widgets = {'name': TextInput(attrs={'type': "text", 'placeholder': 'Введите имя'}),
                   'name2': TextInput(attrs={'type': "text", 'placeholder': 'Введите фамилия'}),
                   'age': TextInput(attrs={'type': "text", 'placeholder': 'Введите возраст'}),
                   'sex': TextInput(attrs={'type': "text", 'placeholder': 'Введите пол'})}