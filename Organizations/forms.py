from django import forms

from .models import Organization, Organization_member



class MOrganizationForm(forms.ModelForm):
	class Meta:
		model = Organization
		fields = ['name', 'description', 'address', 'creator', 'numbers', 'links']



class MOrganization_memberForm(forms.ModelForm):
	class Meta:
		model = Organization_member
		fields = ['id','surname', 'first_name', 'second_name', 'email', 'phone']