from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class BlogArticle(models.Model):
    title = models.CharField(max_length=300,verbose_name='文章标题')
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts',verbose_name='作者')
    body = models.TextField(verbose_name='内容')
    publish_date = models.DateTimeField(default=timezone.now,verbose_name='发布时间')
    update_date =models.DateField(verbose_name='更新时间',blank=True,null=True)

    class Meta:
        ordering = ('-publish_date',)

    def __str__(self):
        return self.title