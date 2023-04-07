from django.urls import path

from . import views

urlpatterns = [
    path('', views.settings, name='settings'),
    path('picture/', views.picture, name='picture'),
    path('password/', views.password, name='password'),
    path('upload_picture/', views.upload_picture, name='upload_picture'),
    path('save_uploaded_picture/', views.save_uploaded_picture, name='save_uploaded_picture'),
]
