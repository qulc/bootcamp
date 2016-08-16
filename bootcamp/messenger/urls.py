from django.conf.urls import url

from .views import inbox, new, send, delete, users, check, messages


urlpatterns = [
    url(r'^$', inbox, name='inbox'),
    url(r'^new/$', new, name='new_message'),
    url(r'^send/$', send, name='send_message'),
    url(r'^delete/$', delete, name='delete_message'),
    url(r'^users/$', users, name='users_message'),
    url(r'^check/$', check, name='check_message'),
    url(r'^(?P<username>[^/]+)/$', messages, name='messages'),
]
