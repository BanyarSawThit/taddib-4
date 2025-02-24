from django import forms
from .models import Customization

class CustomizationForm(forms.ModelForm):
    class Meta:
        model = Customization
        fields = ['meat', 'spice_level']