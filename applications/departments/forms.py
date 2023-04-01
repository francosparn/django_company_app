from django import forms

from .models import Department

class NewDepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = (
            'name',
            'short_name',
            'avatar',
        )
    
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Add name',
                    'class': 'form-control'
                }
            ),
            'short_name': forms.TextInput(
                attrs={
                    'placeholder': 'Add short name',
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