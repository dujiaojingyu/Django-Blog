from django.contrib import admin
from .models import ArticleColumn,ArticlePost
# Register your models here.


admin.site.register(ArticlePost)

class ArticleColumnAdmin(admin.ModelAdmin):
    list_display = ('column','created','user')
    list_filter = ('column',)

admin.site.register(ArticleColumn,ArticleColumnAdmin)