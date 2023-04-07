from django.urls import path

from .import views

urlpatterns = [
    path('', views.feeds, name='feeds'),
    path('<int:pk>/', views.feed, name='feed'),
    path('post/', views.post, name='post'),
    path('like/', views.like, name='like'),
    path('load/', views.load, name='load'),
    path('check/', views.check, name='check'),
    path('update/', views.update, name='update'),
    path('comment/', views.comment, name='comment'),
    path('remove/', views.remove, name='remove_feed'),
    path('load_new/', views.load_new, name='load_new'),
    path('track_comments/', views.track_comments, name='track_comments'),
]
