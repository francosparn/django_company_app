from django import forms

from .models import Employee

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = (
            'first_name',
            'last_name',
            'passport',
            'email',
            'phone',
            'gender',
            'date_of_birth',
            'job',
            'department',
            'avatar',
        )
    
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Add first name'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Add last name'
                }
            ),
            'passport': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Add passport'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Add email'
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Add number phone'
                }
            ),
            'gender': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'date_of_birth': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                    'input_formats': ['%m/%d/%Y %H:%M']
                }
            ),
            'job': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'department': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'avatar': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'type': 'file'
                }
            ),
        }