# Django native imports
from django import forms
from django.contrib import admin
from django.forms import (ModelForm, ValidationError, CharField)
from django.utils.translation import ugettext_lazy as _

# Import from our apps
from money.models import Money

#we need to add form validation here
class MoneyForm(ModelForm):
    class Meta:
        model = Money
        fields = ['date',
                  'amount',
                  'cash',
                  ]
        widgets = {'date': forms.TextInput(attrs={'placeholder': 'Пример: 2018-12-31'})}
    """    
    def __init__(self, *args, **kwargs):
        super(MoneyForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if isinstance(visible.field, forms.BooleanField):
                visible.field.widget.attrs['class'] = 'icheckbox_square-green'
            else:
                visible.field.widget.attrs['class'] = 'form-control'
    """