from django.shortcuts import render
from .models import Book, Author
from . import serializers
from rest_framework import generics

class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer

    class BookDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer
    lookup_url_kwarg = 'id'

    class AuthorListView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = serializers.AuthorSerializer

    def perform_create(self, serializer):
        serializer.save(username=self.request.user)

    class AuthorDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = serializers.AuthorSerializer
    lookup_url_kwarg = 'id'
