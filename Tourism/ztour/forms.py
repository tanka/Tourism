from django import forms
from .models import Contact

# {% if request.user.is_authenticated %} {{ request.user.username }} {% else %} You {% endif %} to Bhutan


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'contact_number', 'message')

class QuickForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email')
