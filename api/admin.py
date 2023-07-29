from django.contrib import admin
from .models import Comment,Post,Like,Follow,Profile
admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Follow)
admin.site.register(Profile)

