from django import forms

class NumberSequenceForm(forms.Form):
    numbers = forms.CharField(
        label="Enter a sequence of numbers (comma-separated)",
        widget=forms.TextInput(attrs={'placeholder': 'e.g., 1,2,3'})
    )
