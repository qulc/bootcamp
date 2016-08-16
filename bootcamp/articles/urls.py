from django.conf.urls import url

from .views import (
    article, articles, write, preview,
    drafts, comment, tag, edit
)

urlpatterns = [
    url(r'^$', articles, name='articles'),
    url(r'^write/$', write, name='write'),
    url(r'^preview/$', preview, name='preview'),
    url(r'^drafts/$', drafts, name='drafts'),
    url(r'^comment/$', comment, name='comment'),
    url(r'^tag/(?P<tag_name>.+)/$', tag, name='tag'),
    url(r'^edit/(?P<article_id>\d+)/$', edit, name='edit_article'),
    url(r'^(?P<slug>[-\w]+)/$', article, name='article'),
]
