from django.contrib import admin
from .models import BlogArticle
# Register your models here.

class BlogArticleAdmin(admin.ModelAdmin):
    list_display = ('title','author','publish_date')
    list_filter = ('publish_date','author')
    search_fields = ('title','author','body')
    raw_id_fields = ('author',)
    date_hierarchy = 'publish_date'
    ordering = ['publish_date','author']

admin.site.register(BlogArticle,BlogArticleAdmin)

