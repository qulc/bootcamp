# Register your models here.
from django.contrib import admin

from .models import Question, Answer, Tag

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Tag)
