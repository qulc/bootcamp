from django.urls import path

from .import views

urlpatterns = [
    path('', views.articles, name='articles'),
    path('write/', views.write, name='write'),
    path('preview/', views.preview, name='preview'),
    path('drafts/', views.drafts, name='drafts'),
    path('comment/', views.comment, name='comment'),
    path('tag/<str:tag_name>/', views.tag, name='tag'),
    path('edit/<int:article_id>/', views.edit, name='edit_article'),
    path('<str:slug>)/', views.article, name='article'),
]
