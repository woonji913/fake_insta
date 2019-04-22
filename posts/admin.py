from django.contrib import admin
from .models import *

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['content',]
admin.site.register(Post, PostAdmin)

class ImageAdmin(admin.ModelAdmin):
    list_display = ['file', 'post_id',]
admin.site.register(Image, ImageAdmin)

class HashtagAdmin(admin.ModelAdmin):
    list_display = ['content',]
admin.site.register(Hashtag, HashtagAdmin)