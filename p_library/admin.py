from django.contrib import admin
from p_library.models import Book
from p_library.models import Author
from p_library.models import Publisher, Inspiration, Friend

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    @staticmethod
    def author_full_name(obj):
        return obj.author.full_name
    list_display = ('title', 'author_full_name','publisher')
    #fields = ('ISBN', 'title', 'description', 'year_release', 'author', 'price', 'publisher', 'authors')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    pass

@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    pass

@admin.register(Inspiration)
class InspirationAdmin(admin.ModelAdmin):
    pass