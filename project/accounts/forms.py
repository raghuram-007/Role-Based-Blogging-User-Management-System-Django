from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Address

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','auto-complete':'off'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','auto-complete':'off'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','auto-complete':'off'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control','auto-complete':'off'}))
    profile_picture = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control','auto-complete':'off'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','auto-complete':'off'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','auto-complete':'off'}))
    
    line1 = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control','auto-complete':'off'}))
    city = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control','auto-complete':'off'}))
    state = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control','auto-complete':'off'}))
    pincode = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control','auto-complete':'off'}))
    
    user_type = forms.ChoiceField(
        choices=(('patient', 'Patient'), ('doctor', 'Doctor')),
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True
    )

    class Meta:
        model = CustomUser
        fields = [
            'first_name', 'last_name', 'username', 'email', 'profile_picture',
            'password1', 'password2', 'user_type', 'line1', 'city', 'state', 'pincode'
        ]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = self.cleaned_data['user_type']
        if commit:
            user.save()
            Address.objects.create(
                user=user,
                line1=self.cleaned_data['line1'],
                city=self.cleaned_data['city'],
                state=self.cleaned_data['state'],
                pincode=self.cleaned_data['pincode']
            )
        return user
