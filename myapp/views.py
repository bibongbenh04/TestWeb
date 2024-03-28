from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages as django_messages
from .models import Feature, quizQuestion, Post, Category, categoryQuiz, Science, Header, Portfolio, Store
from django.core.serializers import serialize
from django.utils.translation import gettext as _
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
	heads = Header.objects.all()
	posts = Post.objects.all()[:5]
	cats = Category.objects.all()

	data = {
		'heads': heads,
		'posts' : posts,
		'cats': cats
	}
	return render(request, 'index.html', data)

# Create your views here.
def science(request):
	heads = Header.objects.all()
	science = Science.objects.all()[:20]
	cats = Category.objects.all()

	data = {
		'heads': heads,
		'sciences' : science,
		'cats': cats
	}
	return render(request, 'science.html', data)

def store(request):
	heads = Header.objects.all()
	stores = Store.objects.all()[:8]
	cats = Category.objects.all()

	data = {
		'heads': heads,
		'stores' : stores,
		'cats': cats
	}
	return render(request, 'store.html', data)

def product(request, url):
	product = Store.objects.get(url=url)
	cats = Category.objects.all()
	return render(request, 'AdminCus/product.html',{'product':product, 'cats': cats})

def about(request):
	heads = Header.objects.all()

	data = {
		'heads': heads,
	}
	return render(request, 'about.html', data)

def dictionaryEL(request):
	return render(request, 'themes/dictionaryEnglish.html')

def load_more_posts(request):
    offset = int(request.GET.get('offset', 0))
    posts = Post.objects.all()[offset:offset+5]  # Lấy 5 bài viết tiếp theo
    return render(request, 'AdminCus/posts.html', {'posts': posts})

def load_more_science(request):
    offset = int(request.GET.get('offset', 0))
    posts = Science.objects.all()[offset:offset+5]  # Lấy 5 bài viết tiếp theo
    return render(request, 'AdminCus/posts.html', {'posts': posts})

def post(request, url):
	post = Post.objects.get(url=url)
	cats = Category.objects.all()
	return render(request, 'AdminCus/tpost.html',{'post':post, 'cats': cats})

def postfillcat(request, url):
    cat = get_object_or_404(Category, url=url)
    cats = Category.objects.all()
    heads = Header.objects.all()  # Thêm dòng này để truy vấn tất cả các Header
    posts = Post.objects.filter(cat=cat)
    return render(request, 'AdminCus/post.html', {'posts': posts, 'cats': cats, 'heads': heads})

def fscience(request, url):
	post = Science.objects.get(url=url)
	cats = Category.objects.all()
	return render(request, 'AdminCus/tpost.html',{'post':post, 'cats': cats})
# def category(request, url):
#     cat = Category.objects.get(url=url)
#     posts = Post.objects.filter(cat=cat)
#     return render(request, "category.html", {'cat': cat, 'posts': posts})

def quiz(request):
    questions = quizQuestion.objects.all()
    questions_list = [
        {
            'question_text': question.question_text,
            'option1': question.choice1,
            'option2': question.choice2,
            'option3': question.choice3,
            'option4': question.choice4,
            'correctChoice': question.correct_choice,
			'url': question.cat.url,
        }
        for question in questions
    ]

    data = {'questions': questions_list, 'category': categoryQuiz.objects.all()}
    
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
