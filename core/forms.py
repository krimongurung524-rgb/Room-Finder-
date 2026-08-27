from django import forms
from .models import Room

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
        
class RoomSearchForm(forms.Form):
    
    # Text field — location search
    location = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Search by location...',
            'class': 'form-input'
        })
    )
    
    # Number field — minimum price
    min_price = forms.DecimalField(
        required=False,
        min_value=0,
        widget=forms.NumberInput(attrs={
            'placeholder': 'Min price (Rs.)',
            'class': 'form-input'
        })
    )
    
    # Number field — maximum price
    max_price = forms.DecimalField(
        required=False,
        min_value=0,
        widget=forms.NumberInput(attrs={
            'placeholder': 'Max price (Rs.)',
            'class': 'form-input'
        })
    )
    
    # Custom validation — euta field ma
    def clean_location(self):
        location = self.cleaned_data.get('location')
        
        # Validation: number matra huna sakdaina
        if location and location.isdigit():
            raise forms.ValidationError(
                "Location number matra huna sakdaina!"
            )
        return location
    
    # Custom validation — duita field milayera (cross-field)
    def clean(self):
        cleaned_data = super().clean()
        min_price = cleaned_data.get('min_price')
        max_price = cleaned_data.get('max_price')
        
        # Validation: min price max bhanda thulo huna sakdaina
        if min_price and max_price:
            if min_price > max_price:
                raise forms.ValidationError(
                    "Minimum price, maximum price bhanda thulo huna sakdaina!"
                )
        return cleaned_data