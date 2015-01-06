from django import forms
from bootcamp.questions.models import Question, Answer
from django.utils.translation import ugettext_lazy as _

class QuestionForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), 
        max_length=255,
        label=_('Title'))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}), 
        max_length=2000,
        label=_('Description'),
        help_text=' ')
    tags = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),
        max_length=255,
        required=False,
        label=_('Tags'),
        help_text=_('Use spaces to separate the tags, such as "asp.net mvc5 javascript"'))

    class Meta:
        model = Question
        fields = ['title', 'description', 'tags']

class AnswerForm(forms.ModelForm):
    question = forms.ModelChoiceField(widget=forms.HiddenInput(), queryset=Question.objects.all())
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'rows':'4'}), 
        max_length=2000)

    class Meta:
        model = Answer
        fields = ['question', 'description']