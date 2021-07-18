from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class UpdatePrizeForm(forms.Form):
    prize_description = forms.CharField(label="Prize:")

    def clean_prize(self):
        data = self.cleaned_data['prize_description']
        # do any checks for validity
        return data


# https://docs.djangoproject.com/en/3.2/ref/forms/fields/
# log in
# sign up (?)
# there should be a prize on the database now

# user profile
    # send kudo
    # rate kudo stars

# org profile
    # edit prize
