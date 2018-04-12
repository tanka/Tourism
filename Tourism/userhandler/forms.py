from django import forms
from django.forms import SelectDateWidget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Tour, Guest


class SignUpForm(UserCreationForm):
    BIRTH_YEAR_CHOICES = range(1920, 1920 + 100, 1)
    birth_date = forms.DateField(
        widget=SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    country = forms.CharField()
    bio = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'birth_date',
                  'password1', 'password2', 'country', 'bio')

class ContactForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    message = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
        help_text='Write here your message!'
    )
    source = forms.CharField(       # A hidden input for internal use
        max_length=50,              # tell from which page the user sent the message
        widget=forms.HiddenInput()
    )

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        message = cleaned_data.get('message')
        if not name and not email and not message:
            raise forms.ValidationError('You have to write something!')

class TourEditForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = ('dateOfArrival', 'duration')
