from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import Profile

# class UserCustomCreationForm(UserCreationForm):
#     class Meta:
#         model = get_user_model()
#         fields = ['username', 'password1', 'password2', 'email',]

class UserCustomChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['email', 'first_name', 'last_name',]
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nickname', 'introduction',]
        
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):  # meta class도 상속받을 수 있다.
        model = get_user_model()
        fields = UserCreationForm.Meta.fields