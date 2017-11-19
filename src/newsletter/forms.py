from django import forms

from .models import SignUp

class ContactForm(forms.Form):
	full_name = forms.CharField(required=False)
	email = forms.EmailField()
	message = forms.CharField()


class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ['full_name','email']
		###exclude = ['full_name'] #you can use this if you have a ton of fields

		#custom validator
		def clean_email(self):
			email = self.cleaned_data.get('email')
			email_base, provider = email.split("@")
			domain, extenstion = provider.split(".")
			"""		
			if not domain == 'ucsc':
				raise forms.ValidationError("Please use a valid Ucsc email address")
			if not extension == "edu":
				raise forms.ValidationError("Please use a valid .edu email address")
			"""
			return email

		def clean_full_name(self):
			full_name = self.cleaned_data.get('full_name')
			#write validation code
			return full_name	