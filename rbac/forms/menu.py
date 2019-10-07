from django import forms
from rbac import models

class MenuModelForm(forms.ModelForm):
    class Meta:
        model = models.Menu
        fields = ['title','icon']
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'icon':forms.RadioSelect(
                choices=[
                    ['x1','xxx1'],
                    ['x2','xxx2']
                ]
            )
        }