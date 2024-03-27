from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.db.models import Q
from django.utils.html import format_html

# from tinymce.models import HTMLField

User = get_user_model()

class Feature(models.Model):
	name = models.CharField(max_length=100)
	details = models.CharField(max_length=500)

class categoryQuiz(models.Model): 
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

class Science(models.Model):
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
    

    
