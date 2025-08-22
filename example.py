import django
import os

# Устанавливаем переменную окружения для настроек Django-проекта
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'book_catalog.settings')

# Инициализируем Django
django.setup()

# Импортируем модели
from books.models import Author, Book, BookDetail
from django.db.models import *

# total_authors = Author.objects.aggregate(total = Count('name')) 

# print(total_authors)
# # author1 = Author.objects.filter()



books =Book.objects.aggregate(total = Count('id'))
print(books)