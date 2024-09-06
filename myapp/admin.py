from django.contrib import admin
from django import forms
from .models import quizQuestion, Category, Post, categoryQuiz, Science, Header, Portfolio, Store, Comment, Community, ProductImage, AccRoblox5k, Subject, Instructor, Course, Chapter, LessonVideo
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.contrib import admin
from .models import Subject, Instructor, Course, Chapter, LessonVideo, LessonNote, LessonResource

class LessonResourceInline(admin.TabularInline):
    model = LessonResource
    extra = 1  # Number of extra resource fields
    fields = ('title', 'file_url')
    readonly_fields = ('id',)  # Only add if you want some fields to be read-only

class LessonNoteInline(admin.TabularInline):
    model = LessonNote
    extra = 1  # Number of extra note fields
    fields = ('user', 'content', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')

class LessonVideoInline(admin.TabularInline):
    model = LessonVideo
    extra = 1  # Số lượng video mặc định để thêm mới
    fields = ('title', 'youtube_link', 'duration', 'order', 'linkggformquiz')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('order',)
# Tùy chỉnh Subject admin
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)
    readonly_fields = ('created_at', 'updated_at')

# Tùy chỉnh Instructor admin
@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('created_at',)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'email', 'bio', 'profile_picture', 'phone_number', 'website')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )

# Tùy chỉnh Course admin
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject', 'start_date', 'end_date', 'price', 'level')
    search_fields = ('title', 'description')
    list_filter = ('subject', 'start_date', 'end_date', 'level')
    filter_horizontal = ('instructors',)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('subject', 'title', 'description', 'start_date', 'end_date', 'price', 'language', 'duration', 'level', 'instructors', 'thumbnail')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )

# Tùy chỉnh Chapter admin
@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'order')
    search_fields = ('title',)
    list_filter = ('course',)
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('course', 'order')
    inlines = [LessonVideoInline]
    fieldsets = (
        (None, {
            'fields': ('course', 'title', 'description', 'order')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )

# Tùy chỉnh LessonVideo admin
@admin.register(LessonVideo)
class LessonVideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'chapter', 'order', 'youtube_link', 'linkggformquiz')
    search_fields = ('title', 'description')
    list_filter = ('chapter__course', 'chapter')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('chapter', 'order')
    fieldsets = (
        (None, {
            'fields': ('chapter', 'title', 'description', 'youtube_link', 'duration', 'order', 'linkggformquiz')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )
    inlines = [LessonResourceInline, LessonNoteInline]

# Register your models here.
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3  # Số lượng form trống hiển thị mặc định

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title', 'description', 'url', 'add_date')
    # list_display = ('title', 'description', 'url', 'add_date')
    search_fields = ('title',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_filter = ('cat',)
    list_per_page = 5

    class Media:
        js = ('https://cdn.tiny.cloud/1/3q1fzzm9ciix8rz2k5kj1v8vwyymlrhnq1a85iji04lb7i0n/tinymce/5/tinymce.min.js','assets/js/TextPost.js',)

class StoreAdmin(admin.ModelAdmin):
    list_display = ( 'nameStore',)
    search_fields = ('nameStore',)
    list_filter = ('cat',)
    list_per_page = 5
    inlines = [ProductImageInline]

    class Media:
        js = ('https://cdn.tiny.cloud/1/3q1fzzm9ciix8rz2k5kj1v8vwyymlrhnq1a85iji04lb7i0n/tinymce/5/tinymce.min.js','assets/js/TextPost.js',)

class AccRoblox5kAdmin(admin.ModelAdmin):
    list_display = ( 'nameStore',)
    search_fields = ('nameStore',)
    list_filter = ('cat',)
    list_per_page = 5
    inlines = [ProductImageInline]

    class Media:
        js = ('https://cdn.tiny.cloud/1/3q1fzzm9ciix8rz2k5kj1v8vwyymlrhnq1a85iji04lb7i0n/tinymce/5/tinymce.min.js','assets/js/TextPost.js',)

# class AccRoblox5kAdminForm(forms.ModelForm):
#     class Meta:
#         model = AccRoblox5k
#         fields = '__all__'

#     def __init__(self, *args, **kwargs):
#         super(AccRoblox5kAdminForm, self).__init__(*args, **kwargs)
#         self.fields['nameStore'].widget.attrs['placeholder'] = 'Tên Sản Phẩm'
#         self.fields['preview_content'].widget.attrs['placeholder'] = 'Mô Tả Xem Trước'
#         self.fields['price_000vnd'].widget.attrs['placeholder'] = 'Đơn Giá(Nghìn Đồng)'
#         self.fields['url'].widget.attrs['placeholder'] = '-> store/url'

class StoreAdminForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(StoreAdminForm, self).__init__(*args, **kwargs)
        self.fields['seller'].widget.attrs['placeholder'] = 'Người Bán Sản Phẩm'
        self.fields['nameStore'].widget.attrs['placeholder'] = 'Tên Sản Phẩm'
        self.fields['numberStore'].widget.attrs['placeholder'] = 'Số Lượng Sản Phẩm'
        self.fields['preview_content'].widget.attrs['placeholder'] = 'Mô Tả Xem Trước'
        self.fields['numberPhone_seller'].widget.attrs['placeholder'] = 'Số Của Người Bán'
        self.fields['link_conection_seller'].widget.attrs['placeholder'] = 'Đường Link Liên Hệ'
        self.fields['price_000vnd'].widget.attrs['placeholder'] = 'Đơn Giá(Nghìn Đồng)'
        self.fields['url'].widget.attrs['placeholder'] = '-> store/url'

# QuizQuestion.objects.all().delete()
admin.site.register(categoryQuiz, CategoryAdmin)
admin.site.register(quizQuestion)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Science, PostAdmin)
admin.site.register(Header)
admin.site.register(Portfolio)
# admin.site.register(Store, StoreAdmin)
# admin.site.register(Store, ProductAdmin)
# admin.site.register(Community, PostAdmin)
@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    form = StoreAdminForm

# @admin.register(AccRoblox5k)
# class AccRoblox5kAdmin(admin.ModelAdmin):
#     form = AccRoblox5kAdminForm



