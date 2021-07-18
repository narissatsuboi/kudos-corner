from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms.widgets import HiddenInput
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
    prize_description = forms.CharField(label="Prize:", max_length=100)

    def clean_prize(self):
        data = self.cleaned_data['prize_description']
        # do any checks for validity
        return data

class SendKudoForm(forms.Form):
    NAME_CHOICES = [(int(user.id), user.name) for user in CustomUser.objects.all()]
    message = forms.CharField(label="Message:", max_length=100)
    recipient = forms.IntegerField(label="Recipient:", widget=forms.Select(choices=NAME_CHOICES))
    
    def clean_message(self):
        data = self.cleaned_data['message']
        return data
    def clean_recipient(self):
        data = self.cleaned_data['recipient']
        return data
    
class RateKudoStars(forms.Form):
    RATING_CHOICES = [(i, i) for i in range(1, 6)]
    id = forms.IntegerField(widget=HiddenInput())
    rating = forms.IntegerField(label="Rating:", widget=forms.Select(choices=RATING_CHOICES))
    def clean_id(self):
        data = self.cleaned_data['id']
        return data
    def clean_rating(self):
        data = self.cleaned_data['rating']
        if data < 1 or data > 5:
            return 3
        else:
            return data
