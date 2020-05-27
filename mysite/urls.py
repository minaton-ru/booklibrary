"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
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