from django.urls import path
from .views import BookListView, BookDetailView, views

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('<uuid:pk>', BookDetailView.as_view(), name='book_detail'),
    path('authors/', views.AuthorListView.as_view(), name="authors"),
    path('author/<int:id>/', views.AuthorDetailsView.as_view(), name="author")
    path('getbooks', views.get_books),
    path('addbook', views.add_book),
    path('updatebook/<int:book_id>', views.update_book),
    path('deletebook/<int:book_id>', views.delete_book)

]

