"""mysite URL Configuration
"""
from django.contrib import admin
from django.urls import include, path
from p_library import views
from p_library import urls
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include(urls.urlpatterns)),
    path('admin/', admin.site.urls),
    path('', views.index),
    path('publisher/', views.publishers),
    path('books/', views.books_list),
    path('books/book_increment/', views.book_increment),
    path('books/book_decrement/', views.book_decrement),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)