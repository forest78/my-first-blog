from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):   #모델을 정의하는 코드 장고모델임을 의미 > 장고는 Post가 데이터베이스에 저장되어야 한다고 알게 됩니다.
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  #다른 모델에 대한 링크

    title = models.CharField(max_length=200)    #글자수가 제한된 텍스트정의 > 글 제목
    text = models.TextField()   #글자수 제한 없음 > 콘텐츠

    created_date = models.DateTimeField(    #날짜, 시간
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
