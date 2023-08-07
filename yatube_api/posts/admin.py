from django.contrib import admin

from .models import Post, Comment, Group


class PostAdmin(admin.ModelAdmin):
    list_display = ['text', 'pub_date', 'author']
    list_filter = ['author', 'pub_date']
    search_fields = ['text']


admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'text', 'post']
    list_filter = ['author', 'created']
    search_fields = ['text']


admin.site.register(Comment, CommentAdmin)


class GroupAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    list_filter = ['title', 'description']
    search_fields = ['title']


admin.site.register(Group, GroupAdmin)
