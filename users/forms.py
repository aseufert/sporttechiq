from django import forms

from showcase.models import Club, Player
import showcase.dropdowns as choices
from users.models import User

from wagtail.users.forms import UserEditForm, UserCreationForm


class CustomUserEditForm(UserEditForm):
    user_type = forms.ChoiceField(choices=choices.user_types, required=True, label='User Type')


class CustomUserCreationForm(UserCreationForm):
    user_type = forms.ChoiceField(choices=choices.user_types, required=True, label='User Type')


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional', label='First Name')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional', label='Last Name')
    email = forms.EmailField(max_length=254, help_text='Valid email address required')
    user_type = forms.ChoiceField(choices=choices.user_types, initial='2', required=True, label='User Type')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'user_type', 'email', 'password1', 'password2')


class RegistrationForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    birth_year = forms.ChoiceField(choices=choices.years, required=True, label='birth_year')
    gender = forms.ChoiceField(choices=choices.genders, required=True, label='gender')
    country = forms.ChoiceField(choices=choices.countries, label='country')
    region = forms.ChoiceField(choices=choices.regions, label='region')
    city = forms.CharField(required=True)
    state = forms.ChoiceField(choices=choices.states, required=True, label='states')
    registration_code = forms.CharField(required=True)

    def clean_registration_code(self):
        data = self.cleaned_data['registration_code']

        if not Club.objects.filter(registration_code=data).exists():
           raise forms.ValidationError('Invalid Registration Code')
        return data

    class Meta:
        model = Player
        fields = ['first_name', 'last_name', 'birth_year', 'gender', 'country', 'region', 'city', 'state', 'user']
