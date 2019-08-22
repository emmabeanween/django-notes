from django import forms

class LoginForm(forms.Form):
	username = forms.CharField(max_length = 40, required=True)
	password = forms.CharField(max_length = 40, required=True, widget=forms.PasswordInput())

class RegisterForm(forms.Form):
	username = forms.CharField(max_length = 40, required=True)
	password = forms.CharField(max_length = 40, required=True, widget=forms.PasswordInput())


class NoteForm(forms.Form):
	title = forms.CharField(max_length = 1000, required=True)
	content = forms.CharField(widget=forms.Textarea(attrs = {'placeholder': 'this is a note where you can place anything that comes to mind.'}), required=True)
