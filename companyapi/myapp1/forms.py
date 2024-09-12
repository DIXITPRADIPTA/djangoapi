from django import forms

class RegistrationForm(forms.Form):
    name=forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(max_length=200,widget=forms.EmailInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')

        if name and len(name) < 9:
            self.add_error('name', 'Name should be at least 9 characters long')