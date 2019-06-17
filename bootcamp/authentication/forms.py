from django import forms
from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


def signup_domain_validator(value):
    if '*' in settings.ALLOWED_SIGNUP_DOMAINS:
        return

    domain = value[value.index("@"):]

    if domain not in settings.ALLOWED_SIGNUP_DOMAINS:
        allowed_domain = ','.join(settings.ALLOWED_SIGNUP_DOMAINS)
        msg = _('Invalid domain. '
                'Allowed domains on this network: {0}').format(allowed_domain)
        raise ValidationError(msg)


def forbidden_username_validator(value):
    forbidden_usernames = {
        'admin', 'settings', 'news', 'about', 'help', 'signin', 'signup',
        'signout', 'terms', 'privacy', 'cookie', 'new', 'login', 'logout',
        'administrator', 'join', 'account', 'username', 'root', 'blog',
        'user', 'users', 'billing', 'subscribe', 'reviews', 'review', 'blog',
        'blogs', 'edit', 'mail', 'email', 'home', 'job', 'jobs', 'contribute',
        'newsletter', 'shop', 'profile', 'register', 'auth', 'authentication',
        'campaign', 'config', 'delete', 'remove', 'forum', 'forums',
        'download', 'downloads', 'contact', 'blogs', 'feed', 'feeds', 'faq',
        'intranet', 'log', 'registration', 'search', 'explore', 'rss',
        'support', 'status', 'static', 'media', 'setting', 'css', 'js',
        'follow', 'activity', 'questions', 'articles', 'network', }
    if value.lower() in forbidden_usernames:
        raise ValidationError(_('This is a reserved word.'))


def invalid_username_validator(value):
    if '@' in value or '+' in value or '-' in value:
        raise ValidationError(_('Enter a valid username.'))


def unique_email_validator(value):
    if User.objects.filter(email__iexact=value).exists():
        raise ValidationError(_('User with this Email already exists.'))


def unique_username_ignore_case_validator(value):
    if User.objects.filter(username__iexact=value).exists():
        raise ValidationError(_('User with this Username already exists.'))


class SignUpForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=30,
        required=True,
        label=_('Username'),
        help_text=_('Usernames may contain alphanumeric, _ and . characters'))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label=_('Password'))
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label=_('Confirm your password'),
        required=True)
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        required=True,
        max_length=75,
        label=_('Email'))

    class Meta:
        model = User
        exclude = ['last_login', 'date_joined']
        fields = ['username', 'email', 'password', 'confirm_password', ]

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].validators += [
            forbidden_username_validator, invalid_username_validator,
            unique_username_ignore_case_validator
        ]
        self.fields['email'].validators += [
            unique_email_validator, signup_domain_validator]

    def clean(self):
        super(SignUpForm, self).clean()
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password and password != confirm_password:
            self._errors['password'] = self.error_class(
                [_('Passwords don\'t match')])
        return self.cleaned_data
