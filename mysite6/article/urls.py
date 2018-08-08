"""mysite6 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url,include
from article import views
from . import list_views
app_name = 'article'
urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^article-column/$', views.article_column,name='article_column'),
    url(r'^rename-column/$', views.rename_acticle_coulmn,name='rename_acticle_coulmn'),
    url(r'^del-column/$', views.del_article_column,name='del_article_column'),
    url(r'^article-post/$', views.article_post,name='article_post'),
    url(r'^article-list/$', views.article_list,name='article_list'),
    url(r'^article-detail/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.article_detail,name='article_detail'),
    url(r'^list-article-detail/(?P<id>\d+)/(?P<slug>[-\w]+)/$', list_views.article_detail,name='list_article_detail'),
    url(r'^del-article/$', views.del_article,name='del_article'),
    url(r'^redit-article/(?P<article_id>\d+)/$', views.redit_article,name='redit_article'),
    url(r'^list-article-titles/$', list_views.article_titles,name='article_titles'),


]
