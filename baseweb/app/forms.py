from django import forms
from app.models import Login_model

class LoginForm(forms.ModelForm):
	class Meta:
		model =Login_model
		fields = '__all__'


