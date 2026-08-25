from django import forms
from core.models import Room

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['title', 'description', 'location', 'price', 'slug']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Room title',
                'class': 'form-input'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Description',
                'class': 'form-input',
                'rows': 4
            }),
            'location': forms.TextInput(attrs={
                'placeholder': 'Location (e.g. Kathmandu)',
                'class': 'form-input'
            }),
            'price': forms.NumberInput(attrs={
                'placeholder': 'Price (Rs.)',
                'class': 'form-input'
            }),
            'slug': forms.TextInput(attrs={
                'placeholder': 'Slug (e.g. cozy-room-1)',
                'class': 'form-input'
            }),
        }