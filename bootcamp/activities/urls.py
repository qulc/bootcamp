from django.urls import path

from .import views

urlpatterns = [
    path('', views.notifications, name='notifications'),
    path('last/', views.last_notifications, name='last_notifications'),
    path('check/', views.check_notifications, name='check_notifications'),
]
