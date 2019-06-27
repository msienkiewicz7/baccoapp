from django import forms
from django.forms import models
from django.forms.fields import MultipleChoiceField
from .models import Sandwich, Ingredient


class MyModelMultipleChoiceField(models.ModelMultipleChoiceField):
    def _get_choices(self):
        if hasattr(self, '_choices'):
            return self._choices
        return MyModelChoiceIterator(self)
    choices = property(_get_choices, MultipleChoiceField._set_choices)


class MyModelChoiceIterator(models.ModelChoiceIterator):
    def choice(self, obj):
        return self.field.prepare_value(obj), self.field.label_from_instance(obj), obj
        # Look at the final item in the return value, it's the object itself that we wanted!


class SandwichForm(forms.ModelForm):
    ingredients = MyModelMultipleChoiceField(
        queryset=Ingredient.objects.all(),
        required=True
    )

    class Meta:
        model = Sandwich
        fields = ('name',
                  'ingredients',
                  'pub_date',
                  'price',
                  )
