from django.contrib import admin
from .models import Post, Comment

admin.site.register(Post)   #관리자 페이지에서 만든모델(Post)보기
admin.site.register(Comment)
