from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.settings, name='settings'),
    url(r'^picture/$', views.picture, name='picture'),
    url(r'^password/$', views.password, name='password'),
    url(r'^upload_picture/$', views.upload_picture, name='upload_picture'),
    url(r'^save_uploaded_picture/$', views.save_uploaded_picture,
        name='save_uploaded_picture'),
]
