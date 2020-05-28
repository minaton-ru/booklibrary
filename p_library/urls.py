from django.contrib import admin  
from django.urls import path  
from .views import AuthorEdit, AuthorList, author_create_many, books_authors_create_many
  
app_name = 'p_library'  

urlpatterns =([
    path('create_author/', AuthorEdit.as_view(), name='author_create'),
    path('authors/', AuthorList.as_view(), name='author_list'),
    path('create_many_authors/', author_create_many, name='author_create_many'),
    path('create_many_books_authors/', books_authors_create_many, name='author_book_create_many'),
], 'p_library')