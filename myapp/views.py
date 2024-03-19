from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages as django_messages
from .models import Feature, QuizQuestion, Post, Category
from django.core.serializers import serialize
from django.utils.translation import gettext as _

# Create your views here.
def index(request):
	features = Feature.objects.all()
	return render(request, 'index.html', {'features' : features})

def dictionaryEL(request):
	return render(request, 'themes/dictionaryEnglish.html')

def homePost(request):
	# load all the post form db(10)
	posts = Post.objects.all()[:11]
	cats = Category.objects.all()
	data = {
		'posts' : posts,
		'cats': cats
	}
	return render(request, 'AdminCus/home.html', data)

def post(request, url):
	post = Post.objects.get(url=url)
	cats = Category.objects.all()
	return render(request, 'AdminCus/post.html',{'post':post, 'cats': cats})

# def category(request, url):
#     cat = Category.objects.get(url=url)
#     posts = Post.objects.filter(cat=cat)
#     return render(request, "category.html", {'cat': cat, 'posts': posts})

def quiz(request):
    questions = QuizQuestion.objects.all()
    questions_list = [
        {
            'question_text': question.question_text,
            'option1': question.choice1,
            'option2': question.choice2,
            'option3': question.choice3,
            'option4': question.choice4,
            'correctChoice': question.correct_choice,
        }
        for question in questions
    ]
    data = {'questions': questions_list}
    
    return render(request, 'quiz.html', {'questions_data': data})
	
def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username=username, password=password)

		if user is not None:
			auth.login(request, user)
			return redirect('/')
		else:
			messages.info(request, 'Credentials Invalid')
			return redirect('login')
	else:
		return render(request, 'themes/login.html')

def logout(request):
	auth.logout(request)
	return redirect('/')

def signup(request):
	if request.method == 'POST':
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		password2 = request.POST['confirm_password']

		if password == password2:
			if User.objects.filter(email=email).exists():
				django_messages.info(request, 'Email Already Used')
				return redirect('signup')
			elif User.objects.filter(username=username).exists():
				django_messages.info(request, 'Username Already Used')
				return redirect('signup')
			else:
				user = User.objects.create_user(username=username, email=email, password=password)
				user.save()
				return redirect('login')
		else:
			django_messages.info(request, 'Password Not The Same')
			return redirect('signup')
	else:
		return render(request, 'themes/signup.html')
