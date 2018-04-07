from django.contrib import admin
from .models import Autor, Publisher, Book



class AuthorAdmin(admin.ModelAdmin):

    search_fields = ['last_name', 'first_name']
    ordering = ['last_name']


class BookAdmin(admin.ModelAdmin):

    search_fields = ['title']
    ordering = ['title']
    list_display = ['title']




# Register your models here.


admin.site.register(Autor, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register([Publisher])
