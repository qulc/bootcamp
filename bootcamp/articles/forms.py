from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Article


class ArticleForm(forms.ModelForm):
    status = forms.CharField(widget=forms.HiddenInput())
    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label=_('Title'),
        max_length=255)
    content = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'}),
        max_length=4000,
        label=_('Content'),
        help_text=" ")
    tags = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=255,
        required=False,
        label=_('Tags'),
        help_text=_(
            'Use spaces to separate the tags, such as "Java Linux Python"'))

    class Meta:
        model = Article
        fields = ['title', 'content', 'tags', 'status']
