from django.contrib import admin
from .models import Article, Comment

admin.site.register(Article)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'article', 'date', 'author', 'active')
    list_filter = ('date','active')
    search_fields = ('author', 'title')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)