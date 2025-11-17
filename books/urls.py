from django.urls import path
from django.shortcuts import redirect
from . import views  # Импортируем views из текущего приложения
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.home_redirect, name='home'),
    path('book_list/', views.book_list, name='book_list'), # Главная страница со списком книг
    path('book/<int:book_id>/', views.book_detail, name='book_detail'), # URL для просмотра конкретной книги по ID
    path('search/', views.search_books, name='search'), # URL для страницы поиска книг
    path('signup/', views.signup, name='signup'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout')
]
