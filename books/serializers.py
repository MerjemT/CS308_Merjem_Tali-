from rest_framework import serializers

from books.models import Book, Author

class BookSerializer(serializers.ModelSerializer):
    """Serializer for the book objects"""

    class Meta:
        model = Book
        fields = (
                'id', 'title', 'authors', 
                'publisher', 'publication_date',
                'number_of_pages'
        )
        read_only_fields = ('id',)



class AuthorSerializer(serializers.ModelSerializer):
    """Serializer for the author objects"""

    books = serializers.PrimaryKeyRelatedField(many=True, queryset=Book.objects.all())

    class Meta:
        model = Author
        fields = (
                'id', 'name', 'username', 'books'
        )
        read_only_fields = ('id','books','username')
