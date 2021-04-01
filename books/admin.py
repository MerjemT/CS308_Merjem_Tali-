from django.contrib import admin
from .models import Book, Review


class ReviewInline(admin.TabularInline):
    model = Review


class BookAdmin(admin.ModelAdmin):
    inlines = [
        ReviewInline,
        ]
    list_display = ('title', 'author', 'publication_date', 'number_of_pages')


admin.site.register(Book, BookAdmin)
