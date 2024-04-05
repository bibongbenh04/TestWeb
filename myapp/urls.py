from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
	path('', views.index, name = 'index'),
	path('science', views.science, name = 'science'),
	# path('community', views.community, name = 'community'),
	path('login', views.login, name = 'login'),
	path('signup', views.signup, name = 'signup'),
	path('logout', views.logout, name = 'logout'),
	path('changepass', views.change_password, name = 'changepass'),
	path('quiz', views.quiz, name = 'quiz'),
	path('store', views.store, name = 'store'),
    path('blog/<slug:url>', views.post, name='blog'),
#    path('community/<slug:url>', views.fcommunity, name='fcommunity'),
    path('category/<slug:url>', views.postfillcat),
    path('science/<slug:url>', views.fscience, name = 'science'),
    path('product/<slug:url>', views.product),
    path('SearchByName', views.searchByName, name = 'searchbyname'),
    path('SearchStoreByName', views.searchStoreByName, name = 'searchstorebyname'),
	path('load-more-posts/', views.load_more_posts, name='load_more_posts'),
	path('load-more-sciences/', views.load_more_sciences, name='load_more_sciences'),
	path('dictionaryEL', views.dictionaryEL, name = 'dictionaryEL'),
	path('about', views.about, name = 'about'),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)