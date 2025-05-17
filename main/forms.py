from django import forms
from .models import Item, Rim, Print

# Forms 
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = "__all__"

class RimForm(forms.ModelForm):
    class Meta:
        model = Rim
        fields = '__all__'

class PrintForm(forms.ModelForm):
    class Meta:
        model = Print
        fields = '__all__'