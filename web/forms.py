from django.forms import ModelForm
from .models import Record
from django import forms

INPUT_CLASS='w-full px-6 py-4 rounded-xl border '
class RecordForm(ModelForm):
    class Meta:
        model=Record
        fields=['first_name','last_name','departments','address','email','phone','city','zipcode']
        widgets={
       'first_name':forms.TextInput(attrs={
       'class':INPUT_CLASS,
       'placeholder':'Enter first_name'
       }),
       'last_name':forms.TextInput(attrs={
       'class':INPUT_CLASS,
       'placeholder':'Enter last_name'
       }),
       'departments':forms.Select(attrs={
       'class':INPUT_CLASS,
       'placeholder':'Select department'
       }),
       'address':forms.TextInput(attrs={
       'class':INPUT_CLASS,
       'placeholder':'Enter address'
       }),
       'email':forms.EmailInput(attrs={
       'class':INPUT_CLASS,
       'placeholder':'Enter email address'
       }),
       'phone':forms.TextInput(attrs={
            'class':INPUT_CLASS,
            'placeholder':'Enter phone number'
       }),
       'city':forms.TextInput(attrs={
            'class':INPUT_CLASS,
            'placeholder':'Enter your city'
       }),
       'zipcode':forms.TextInput(attrs={
            'class':INPUT_CLASS,
            'placeholder':'Enter your zipcode',
       })
      } 

    