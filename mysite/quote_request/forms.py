from django import forms
from .models import QuoteRequest

# quote request form
class QuoteRequestForm(forms.ModelForm):
    class Meta:
        model = QuoteRequest
        fields = ['name', 'email', 'phone', 'industry', 'message']