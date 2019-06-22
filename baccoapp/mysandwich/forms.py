from django import forms
from .models import Sandwich

class SandwichForm(forms.ModelForm):
    class Meta:
        model = Sandwich
        fields = ('name',
                  'ingredients',
                  'pub_date',
                  'price',
                  )
