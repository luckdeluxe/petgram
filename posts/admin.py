from django.contrib import admin
from django.contrib.auth.models import User
from posts.models import Post



# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """post admin model"""
    list_display = ('user','title','photo','created', 'modified',)
    list_display_links= ('title',)

    search_fields = ('user__username', 'title','created')

    list_filter = ('created', 'modified')

