from django.contrib import admin
from django import forms
from .models import QuizQuestion, Category, Post
from django.core.exceptions import ValidationError
from django.db.models import Q
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title', 'description', 'url', 'add_date')
    search_fields = ('title',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_filter = ('cat',)
    list_per_page = 5

    class Media:
        js = ('https://cdn.tiny.cloud/1/3q1fzzm9ciix8rz2k5kj1v8vwyymlrhnq1a85iji04lb7i0n/tinymce/5/tinymce.min.js','assets/js/TextPost.js',)

admin.site.register(QuizQuestion)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)