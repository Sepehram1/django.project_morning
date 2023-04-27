from django.contrib import admin
from sun.models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_posted')
    list_filter = ('date_posted',)
    search_fields = ('title', 'content')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('post', 'author', 'text')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
