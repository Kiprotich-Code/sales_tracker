from django import forms
from .models import Item, Rim, Print

# Forms 
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = "__all__"