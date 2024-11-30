from django.contrib import admin
from .models import Book, Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'book', 'text', 'datetime_created', 'is_active']

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'price', 'user']

# Register your models here.
admin.site.register(Book, BookAdmin)
admin.site.register(Comment, CommentAdmin)