from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.db.models import Q
from django.utils.html import format_html
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils.text import slugify
from unidecode import unidecode
# from tinymce.models import HTMLField

User = get_user_model()
from django.db import models

def custom_slugify(value):
    value = unidecode(value)
    value = slugify(value, allow_unicode=True)  # Giữ lại các ký tự Unicode
    return value.replace('_', '-')  # Thay thế dấu gạch dưới bằng dấu gạch nối

# Model cho lĩnh vực dạy học
class Subject(models.Model):
    is_active = models.BooleanField(default=True)
    url = models.SlugField(max_length=100, unique=True, blank=True, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.url:
            # Tạo slug từ tên
            self.url = custom_slugify(self.name)
            print(self.url)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

# Model cho giảng viên
class Instructor(models.Model):
    is_active = models.BooleanField(default=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='instructors/', null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Model cho khóa học
class Course(models.Model):
    is_active = models.BooleanField(default=True)
    url = models.SlugField(max_length=100, unique=True, blank=True)
    subject = models.ForeignKey(Subject, related_name='courses', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    language = models.CharField(max_length=50, default='Vietnamese')
    duration = models.CharField(max_length=50)  # Example: "6 weeks", "3 months"
    level = models.CharField(max_length=50, choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')])
    instructors = models.ManyToManyField(Instructor, related_name='courses')
    thumbnail = models.ImageField(upload_to='course_thumbnails/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.url:
            # Tạo slug từ tiêu đề
            self.url = custom_slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

# Model cho chương học trong khóa học
class Chapter(models.Model):
    is_active = models.BooleanField(default=True)
    course = models.ForeignKey(Course, related_name='chapters', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    order = models.PositiveIntegerField()  # Order of the chapter in the course
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    url = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.url:
            # Tạo slug từ tiêu đề
            self.url = custom_slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Chapter {self.order}: {self.title}"

# Model cho video bài học trong chương học
class LessonVideo(models.Model):
    is_active = models.BooleanField(default=True)
    chapter = models.ForeignKey(Chapter, related_name='videos', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    youtube_link = models.URLField()
    duration = models.DurationField(null=True, blank=True)  # Duration of the video
    order = models.PositiveIntegerField()  # Order of the video in the chapter
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    url = models.SlugField(max_length=100, unique=True, blank=True)
    linkggformquiz = models.URLField(null=True)

    def save(self, *args, **kwargs):
        if not self.url:
            # Tạo slug từ tiêu đề
            self.url = custom_slugify(self.title)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"Lesson {self.order}: {self.title}"

class LessonResource(models.Model):
    lesson = models.ForeignKey(LessonVideo, related_name='resources', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    file_url = models.URLField(max_length=500, blank=True)  

    def __str__(self):
        return self.title

class LessonNote(models.Model):
    lesson = models.ForeignKey(LessonVideo, related_name='notes', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='notes', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Note by {self.user.username} on {self.lesson.title}"

class Feature(models.Model):
	name = models.CharField(max_length=100)
	details = models.CharField(max_length=500)

class categoryQuiz(models.Model): 
    TYPE_CATEGORY_QUIZ = [
        ('TEST ONL', 'TEST ONL'),
        ('CONTEST', 'CONTEST'),
    ]
    typeCate = models.CharField(max_length=10, choices=TYPE_CATEGORY_QUIZ, default = 'TEST ONL')
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='category/')
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.CharField(max_length=100, unique=True)
    add_date = models.DateTimeField(auto_now_add=True, null=True)

    
    def image_tag(self):
        return format_html('<img src="/media/{}" style = "width:40px;height:40px;border-radius:50%" />'.format(self.image))
        
    def __str__(self):
        return self.title   

class quizQuestion(models.Model):
    is_active = models.BooleanField(default=True)
    cat = models.ForeignKey(categoryQuiz, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    choice1 = models.CharField(max_length=200)
    choice2 = models.CharField(max_length=200)
    choice3 = models.CharField(max_length=200)
    choice4 = models.CharField(max_length=200)
    correct_choice = models.IntegerField(choices=[(1, 'Choice 1'), (2, 'Choice 2'), (3, 'Choice 3'), (4, 'Choice 4')])

    def __str__(self):
        return self.question_text

#Category model
class Category(models.Model):
    is_active = models.BooleanField(default=True)
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='category/')
    add_date = models.DateTimeField(auto_now_add=True, null=True)

    def image_tag(self):
        return format_html('<img src="/media/{}" style = "width:40px;height:40px;border-radius:50%" />'.format(self.image))
    
    def __str__(self):
        return self.title   

class Post(models.Model):
    is_active = models.BooleanField(default=True)
    author = models.CharField(max_length=30)
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    # content = HTMLField()
    content = models.TextField()
    preview_content = models.CharField(max_length=1000, blank=False)
    url = models.CharField(max_length=100, unique=True)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post/')
    add_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    name = models.CharField(max_length=225)
    body = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, default=None, null=True)
    object_id = models.PositiveIntegerField(default=None, null=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f"{self.name} - {self.date}"

class Science(models.Model):
    is_active = models.BooleanField(default=True)
    author = models.CharField(max_length=30)
    science_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    preview_content = models.CharField(max_length=1000, blank=False)
    url = models.CharField(max_length=100, unique=True)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post/')
    add_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title
    
class Community(models.Model):
    TYPE_CHOICES = [
        ('Khác', 'Khác'),
        ('Góp Ý', 'Góp Ý'),
        ('Chia Sẽ', 'Chia Sẽ'),
        ('Kiến Thức', 'Kiến Thức'),
    ]
    is_active = models.BooleanField(default=True)
    author = models.CharField(max_length=30)
    community_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    url = models.CharField(max_length=100, unique=True)
    cat = models.CharField(max_length=100, choices = TYPE_CHOICES)
    image = models.ImageField(upload_to='post/')
    add_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

class Store(models.Model):
    is_active = models.BooleanField(default=True)
    seller = models.CharField(max_length=30)
    store_id = models.AutoField(primary_key=True)
    nameStore = models.CharField(max_length=200)
    numberStore = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    content = models.TextField()
    preview_content = models.CharField(max_length=1000, blank=False)
    numberPhone_seller = models.DecimalField(max_digits=10, decimal_places=0, default=0000000000)
    link_conection_seller = models.CharField(max_length=100)
    price_000vnd = models.DecimalField(max_digits=10, decimal_places=2)
    url = models.CharField(max_length=100, unique=True)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    # image = models.ImageField(upload_to='store/', default=None, blank=False)
    add_date = models.DateTimeField(auto_now_add=True, null=True)

    def image_tag(self):
        return format_html('<img src="/media/{}" style = "width:auto;height:100px;border-radius:40%;filter: drop-shadow(1px 1px 20px green)" />'.format(self.image))

    def __str__(self):
        return self.nameStore
    
class AccRoblox5k(models.Model):
    username = models.CharField(max_length=100, unique=True, null=False)
    password = models.CharField(max_length=100, null=False)
    is_active = models.BooleanField(default=True)
    store_id = models.AutoField(primary_key=True)
    nameStore = models.CharField(max_length=200, default="MÃ SỐ: A5K-")
    content = models.TextField(default="Đây là Tài Khoản Roblox Bloxfruit 5k")
    preview_content = models.CharField(max_length=1000, blank=False, default="MỤC: RANDOM5K")
    price_000vnd = models.DecimalField(max_digits=10, decimal_places=2, default="5.00")
    url = models.CharField(max_length=100, unique=True)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE, default="Acc Roblox 5k")
    image = models.ImageField(upload_to='store/', blank=True, default= "store/background-playlist_lxw56b")
    add_date = models.DateTimeField(auto_now_add=True, null=True)

    def image_tag(self):
        return format_html('<img src="/media/{}" style = "width:auto;height:100px;border-radius:40%;filter: drop-shadow(1px 1px 20px green)" />'.format(self.image))

    def __str__(self):
        return self.nameStore

class ProductImage(models.Model):
    product = models.ForeignKey(Store, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='store/')
    preview_content = models.CharField(max_length=1000, default="None", blank=False)

    def __str__(self):
        return f"Image for {self.product.nameStore}"

class Header(models.Model):
    is_active = models.BooleanField(default=True)
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    # logo = models.ImageField(upload_to='header_logos/'

    def __str__(self):
        return self.title

class Portfolio(models.Model):
    is_active = models.BooleanField(default=True)
    TYPE_CHOICES = [
        ('Card', 'Card'),
        ('App', 'App'),
        ('Web', 'Web'),
    ]
    typeP = models.CharField(max_length=4, choices=TYPE_CHOICES)
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    # logo = models.ImageField(upload_to='header_logos/'

    def __str__(self):
        return self.title

    

    

    
