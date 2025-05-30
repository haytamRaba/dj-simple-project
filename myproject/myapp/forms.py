from django import forms
# inherit from forms.Form
class CreateNewList(forms.Form):
	name = forms.CharField(label="Name",max_length=200)
	check = forms.BooleanField(required=False)