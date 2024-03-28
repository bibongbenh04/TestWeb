from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
	path('', views.index, name = 'index'),
	path('science', views.science, name = 'science'),
	path('login', views.login, name = 'login'),
	path('signup', views.signup, name = 'signup'),
	path('logout', views.logout, name = 'logout'),
	path('quiz', views.quiz, name = 'quiz'),
	path('store', views.store, name = 'store'),
    path('blog/<slug:url>', views.post),
    path('category/<slug:url>', views.postfillcat),
    path('science/<slug:url>', views.fscience),
    path('product/<slug:url>', views.product),
	path('load-more-posts/', views.load_more_posts, name='load_more_posts'),
	path('dictionaryEL', views.dictionaryEL, name = 'dictionaryEL'),
	path('about', views.about, name = 'about'),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)