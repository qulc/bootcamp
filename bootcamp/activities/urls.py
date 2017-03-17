from django.conf.urls import url

from .import views

urlpatterns = [
    url(r'^$', views.notifications, name='notifications'),
    url(r'^last/$', views.last_notifications, name='last_notifications'),
    url(r'^check/$', views.check_notifications, name='check_notifications'),
]
