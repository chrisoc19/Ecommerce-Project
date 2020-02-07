from django import forms

Small = 'S'
Medium = 'M'
Large = 'L'
SIZE_CHOICES = [
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large')
]


class SizeForm(forms.Form):
    
    size = forms.CharField(label='Sizes',  widget=forms.Select(choices=SIZE_CHOICES))

