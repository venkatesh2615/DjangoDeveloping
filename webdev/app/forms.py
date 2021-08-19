from django import forms

class CreateList(forms.Form):
    name=forms.CharField(label='Name',max_length='32')
    check=forms.BooleanField(required=False)




