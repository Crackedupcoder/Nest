from django.contrib import admin
from .models import  Post, HomePageCoverImage, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','author','tags','slug','status','publish']
    list_filter = ['status','created','author','publish']
    search_fields = ['title','body']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status','publish']



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'active', 'created']
    list_filter = ['active', 'created', 'updated']
    search_fields = ['user', 'post', 'body']


admin.site.register(HomePageCoverImage)


