# books/views.py
from django.shortcuts import render, get_object_or_404 ,redirect
from django.db.models import Q
from .models import Book
from .forms import *
from django.contrib.auth import login
from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required

def home_redirect(request):
    if request.user.is_authenticated:
        return redirect('book_list')
    return redirect('login')

@login_required
def book_list(request): 
    books = Book.objects.all() # Получаем всю информацию из таблицы Book

    # Передаем ее в еще не существующий шаблон book_list.html
    return render(request, 'books/book_list.html', {'books': books})

@login_required
def book_detail(request, book_id): 
    # Получаем информацию о книге по id, если не найдено, на странице возникает ошибка 404 Not found
    book = get_object_or_404(Book, id=book_id) 

    # Передаем ее в еще не существующий шаблон book_detail.html
    return render(request, 'books/book_detail.html', {'book': book})


def search_books(request): 
    query = request.GET.get('q', '') # Получаем содержимое запроса 
    query = query.strip().lower() # Приводим строку к нижнему регистру и удаляем лишние пробелы
	
    if query: 
        words = query.split()  # Разбиваем строку запроса на отдельные слова
        filters = Q() # Создаем объект фильтра, чтобы применить его в дальнейшем

        for word in words:
            filters |= Q(title__icontains=word)  # Добавляем фильтр поиска по заголовку книги
	      # (Оператор |= используется для объединения условий в Q()-объекте с помощью логического ИЛИ)

        books = Book.objects.filter(filters) # Фильтруем книги по составному запросу
    else:
        books = []

    # Передаем полученную информацию в еще не существующий шаблон search.html
    return render(request, 'books/search.html', {'books': books})



def signup(request): #регистрация логина
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Вход сразу после регистрации
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


from django.contrib.auth.views import LoginView
class CustomLoginView(LoginView):#вход
    template_name = 'registration/login.html'
    

@login_required
def profile(request):
    return render(request, 'registration/profile.html')