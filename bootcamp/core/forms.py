from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=30, label=_('First Name'), required=False)
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=30, label=_('Last Name'), required=False)
    job_title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=50, label=_('Job Title'), required=False)
    email = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=75, label=_('Email'), required=False)
    url = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=50, label=_('Url'), required=False)
    location = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=50, label=_('Location'), required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'job_title', 'email', 'url',
                  'location', ]


class ChangePasswordForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput())
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label=_("Old password"), required=True)
    new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label=_("New password"), required=True)
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label=_("Confirm new password"), required=True)

    class Meta:
        model = User
        fields = ['id', 'old_password', 'new_password', 'confirm_password']

    def clean(self):
        super(ChangePasswordForm, self).clean()

        old_password = self.cleaned_data.get('old_password')
        new_password = self.cleaned_data.get('new_password')
        confirm_password = self.cleaned_data.get('confirm_password')

        user_id = self.cleaned_data.get('id')
        user = User.objects.get(pk=user_id)

        if not user.check_password(old_password):
            self._errors['old_password'] = self.error_class(
                ['Old password don\'t match'])

        if new_password and new_password != confirm_password:
            self._errors['new_password'] = self.error_class(
                ['Passwords don\'t match'])

        return self.cleaned_data


class SavePictureForm(forms.Form):
    x = forms.IntegerField(min_value=0)
    y = forms.IntegerField(min_value=0)
    width = forms.IntegerField(min_value=0)
    height = forms.IntegerField(min_value=0)
