from django.urls import path

from . import views


urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('new/', views.new, name='new_message'),
    path('send/', views.send, name='send_message'),
    path('delete/', views.delete, name='delete_message'),
    path('users/', views.users, name='users_message'),
    path('check/', views.check, name='check_message'),
    path('<str:username>/', views.messages, name='messages'),
]
