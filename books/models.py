from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Author(models.Model): 
    name = models.CharField(max_length=150)
    img_src = models.URLField(blank=True,null=True)
    years_of_age = models.CharField(max_length=50)
    bio = models.TextField()
    works = models.TextField(blank=True,null=True)
    number = models.IntegerField()

    class Meta:
        db_table = 'author'
        ordering = ['name']
    
    def __str__(self):
        return self.name



class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(Author,on_delete = models.CASCADE, related_name = 'books',blank=True,null = True)
    img_src = models.URLField(blank=True,null=True)
    publication_date = models.DateField()
    short_desc = models.TextField()

    class Meta:
        db_table = 'book'
        ordering = ['title']
    
    def __str__(self):
        return self.title
    

class BookDetail(models.Model):
    book = models.OneToOneField(Book,on_delete= models.CASCADE,related_name='details')
    description = models.TextField()

    class Meta:
        db_table = 'book_detail'
    
    def __str__(self):
        return f'Детали о книге {self.book.title}'
    

class user(models.Model):
    username = models.CharField(max_length=125)
    password = models.CharField()
    email = models.EmailField()
    first_name = models.CharField()
    last_name = models.CharField()


    def __str__(self):
        return self.name


