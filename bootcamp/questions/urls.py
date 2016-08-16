from django.conf.urls import url

from .views import (
    question, answer, answered, unanswered, ask,
    all_question, questions, favorite, accept, vote
)

urlpatterns = [
    url(r'^$', questions, name='questions'),
    url(r'^answered/$', answered, name='answered'),
    url(r'^unanswered/$', unanswered, name='unanswered'),
    url(r'^all/$', all_question, name='all'),
    url(r'^ask/$', ask, name='ask'),
    url(r'^favorite/$', favorite, name='favorite'),
    url(r'^answer/$', answer, name='answer'),
    url(r'^answer/accept/$', accept, name='accept'),
    url(r'^answer/vote/$', vote, name='vote'),
    url(r'^(\d+)/$', question, name='question'),
]
