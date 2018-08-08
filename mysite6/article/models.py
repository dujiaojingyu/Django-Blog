from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.shortcuts import reverse
from slugify import slugify
# Create your models here.


class ArticleColumn(models.Model):
    user = models.ForeignKey(User,related_name='article_column',on_delete=models.CASCADE)
    column = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.column



class ArticlePost(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='article')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=500)
    column = models.ForeignKey(ArticleColumn,on_delete=models.CASCADE,related_name='article_column')
    body = models.TextField()
    created_data = models.DateTimeField(default=timezone.now)
    updated_data = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-updated_data',)
        index_together = (('id','slug'),)
    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(ArticlePost,self).save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse("article:article_detail",args=[self.id,self.slug])

    def get_url_path(self):
        return reverse('article:list_article_detail',args=[self.id,self.slug])