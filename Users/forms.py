from django import forms

from .models import User



class MUserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['surname', 'first_name',
		'second_name', 'email', 'phone', 'address']