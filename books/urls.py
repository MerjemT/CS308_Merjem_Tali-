from django.urls import path
from .views import BookListView, BookDetailView

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('<uuid:pk>', BookDetailView.as_view(), name='book_detail'),
    path('authors/', views.AuthorListView.as_view(), name="authors"),
    path('author/<int:id>/', views.AuthorDetailsView.as_view(), name="author")
]

