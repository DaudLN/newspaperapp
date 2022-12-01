
from django.contrib import admin

from .models import Article, Comment

# Register your models here.

# admin.site.register(Article)
# admin.site.register(Comment)

# Inlines


class CommentInline(admin.TabularInline):
    model = Comment
    extra: int = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    model = Article
    # fields = ['title', 'author']
    inlines = [CommentInline]


@admin.register(Comment)
class ArticleAdmin(admin.ModelAdmin):
    model = Comment
