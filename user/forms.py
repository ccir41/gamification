from django import forms

from .models import User


class SignInForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput())


class SignUpForm(forms.ModelForm):
    password = forms.CharField(min_length=8, widget=forms.PasswordInput(
        attrs={'placeholder': 'password'}))
    confirm_password = forms.CharField(min_length=8, widget=forms.PasswordInput(
        attrs={'placeholder': 'repeat password'}))
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'confirm_password', 'what_best_describe_you', )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            self.add_error("password", forms.ValidationError(
                "Passwords didn't matched!"))
            self.add_error("confirm_password", forms.ValidationError(
                "Passwords didn't matched!"))
        return cleaned_data

    def save(self):
        username = self.cleaned_data.get('email')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        what_best_describe_you = self.cleaned_data.get('what_best_describe_you')
        return User.objects.create_user(username=username, email=email, password=password, what_best_describe_you=what_best_describe_you)