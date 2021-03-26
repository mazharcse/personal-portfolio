from django.contrib import admin
from blog.models import Post, Category, Comment
# Register your models here.
#
#
# class PostAdmin(admin.ModelAdmin):
#     pass
#
#
# class CategoryAdmin(admin.ModelAdmin):
#     pass


admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)
