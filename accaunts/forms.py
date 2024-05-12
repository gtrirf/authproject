from django import forms
from accaunts.models import CostumerUsers


class UsersForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CostumerUsers
        fields = ('username', 'email', 'first_name', 'last_name', 'password', 'image')

    def save(self, commit=True):
        user = super().save(commit=True)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

