from django import forms
from models import participante

class participante_form(forms.ModelForm):
   class Meta:
      model = participante