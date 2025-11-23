from django import forms
from .models import Post
from django import forms
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image', 'category', 'summary', 'content', 'status']



# class DoctorSignupForm(forms.ModelForm):
#     username = forms.CharField(max_length=150)
#     password = forms.CharField(widget=forms.PasswordInput)
#     email = forms.EmailField(required=True)

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data['password'])
#         if commit:
#             user.save()
#             UserProfile.objects.create(user=user, role='doctor')
#         return user


# class PatientSignupForm(forms.ModelForm):
#     username = forms.CharField(max_length=150)
#     password = forms.CharField(widget=forms.PasswordInput)
#     email = forms.EmailField(required=True)

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data['password'])
#         if commit:
#             user.save()
#             UserProfile.objects.create(user=user, role='patient')
#         return user
