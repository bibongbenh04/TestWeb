from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages as django_messages
from .models import Feature, quizQuestion, Post, Category, categoryQuiz, Science, Header, Portfolio, Store, Comment
from django.core.serializers import serialize
from django.utils.translation import gettext as _
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


# Create your views here.
def index(request):
	heads = Header.objects.filter(is_active = True)
	posts = Post.objects.all()[:5]
	cats = Category.objects.filter(is_active = True)

	data = {
		'heads': heads,
		'posts' : posts,
		'cats': cats
	}
	return render(request, 'index.html', data)

# Create your views here.
def science(request):
	heads = Header.objects.filter(is_active = True)
	science = Science.objects.filter(is_active = True)[:5]
	cats = Category.objects.filter(is_active = True)

	data = {
		'heads': heads,
		'sciences' : science,
		'cats': cats
	}
	return render(request, 'science.html', data)

def load_more_sciences(request):
    offset = int(request.GET.get('offset', 0))
    posts = Science.objects.all()[offset:offset+5]  # Lấy 5 bài viết tiếp theo
    return render(request, 'AdminCus/posts.html', {'posts': posts})

def store(request):
	heads = Header.objects.filter(is_active = True)
	stores = Store.objects.filter(is_active = True)[:8]
	cats = Category.objects.filter(is_active = True)

	data = {
		'heads': heads,
		'stores' : stores,
		'cats': cats
	}
	return render(request, 'store.html', data)


def searchByName(request):
	heads = Header.objects.filter(is_active = True)
	query = request.GET.get('query', '')
	posts = Post.objects.filter(title__icontains=query)[:5]
	sciences = Science.objects.filter(title__icontains=query)[:5]
	context = {
		'sciences':sciences,
		'heads': heads,
        'posts': posts,  # Giả sử kết quả tìm kiếm của bạn
        'query': query,
    }
	return render(request, 'AdminCus/post.html', context)

def searchStoreByName(request):
	heads = Header.objects.filter(is_active = True)
	query = request.GET.get('query', '')
	stores = Store.objects.filter(nameStore__icontains=query)[:8]
	context = {
		'heads': heads,
		'product': product,
        'stores': stores,  # Giả sử kết quả tìm kiếm của bạn
        'query': query,
    }
	return render(request, 'store.html', context)

def product(request, url):
	product = Store.objects.get(url=url)
	cats = Category.objects.filter(is_active = True)
	return render(request, 'AdminCus/product.html',{'product':product, 'cats': cats})

def about(request):
	heads = Header.objects.filter(is_active = True)

	data = {
		'heads': heads,
	}
	return render(request, 'about.html', data)

def dictionaryEL(request):
	return render(request, 'themes/dictionaryEnglish.html')


def post(request, url):
    post = Post.objects.get(url=url)
    get_all_comments = Comment.objects.filter(post_name=post)
    number_of_comments = 0
    for _ in get_all_comments:
        number_of_comments += 1

    if request.method == 'POST':
        name = request.POST['name']
        body = request.POST['body']
        new_comment = Comment(name=name, post_name=post, body=body)  # Corrected variable name
        new_comment.save()
        django_messages.success(request, 'Bình Luận Của Bạn Đã Được Thêm Vào !')
        return redirect('blog', url=url)
    
    cats = Category.objects.filter(is_active=True)
    return render(request, 'AdminCus/tpost.html', {'post': post, 'cats': cats, 'comments': get_all_comments, 'number_of_comments': number_of_comments})


def load_more_posts(request):
    offset = int(request.GET.get('offset', 0))
    posts = Post.objects.all()[offset:offset+5]  # Lấy 5 bài viết tiếp theo
    return render(request, 'AdminCus/posts.html', {'posts': posts})

def postfillcat(request, url):
    cat = get_object_or_404(Category, url=url)
    cats = Category.objects.filter(is_active = True)
    heads = Header.objects.filter(is_active = True)  # Thêm dòng này để truy vấn tất cả các Header
    posts = Post.objects.filter(cat=cat)
    return render(request, 'AdminCus/post.html', {'posts': posts, 'cats': cats, 'heads': heads})

def fscience(request, url):
	post = Science.objects.get(url=url)
	cats = Category.objects.filter(is_active = True)
	return render(request, 'AdminCus/tpost.html',{'post':post, 'cats': cats})
# def category(request, url):
#     cat = Category.objects.get(url=url)
#     posts = Post.objects.filter(cat=cat)
#     return render(request, "category.html", {'cat': cat, 'posts': posts})

def quiz(request):
    questions = quizQuestion.objects.filter(is_active = True)
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
			storage = django_messages.get_messages(request)
			storage.used = True
			django_messages.info(request, 'Thông tin đăng nhập chưa chính xác !')
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
				django_messages.info(request, 'Email Đã Được Sử Dụng')
				return redirect('signup')
			elif User.objects.filter(username=username).exists():
				django_messages.info(request, 'Username Đã Được Sử Dụng')
				return redirect('signup')
			else:
				user = User.objects.create_user(username=username, email=email, password=password)
				user.save()
				return redirect('login')
		else:
			django_messages.info(request, 'Mật Khẩu Không Trùng')
			return redirect('signup')
	else:
		return render(request, 'themes/signup.html')
	
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Cập nhật session để tránh đăng xuất
            django_messages.success(request, 'Mật khẩu của bạn đã được thay đổi thành công!')
            return redirect('/')
        else:
            django_messages.error(request, 'Vui lòng sửa lại các lỗi bên dưới.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'themes/changePass.html', {'form': form})
