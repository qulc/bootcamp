from django.contrib import admin

from .models import Article, Tag, ArticleComment

admin.site.register(Article)
admin.site.register(Tag)
admin.site.register(ArticleComment)
