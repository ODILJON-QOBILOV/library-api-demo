from django.urls import path
from .views import BookListApiView, BookCreateApiView, BookDetailApiView, BookDeleteApiView, BookUpdateApiView

urlpatterns = [
    path('books/', BookListApiView.as_view()),
    path('books/create/', BookCreateApiView.as_view()),
    path('books/<int:pk>/', BookDetailApiView.as_view()),
    path('books/delete/<int:pk>/', BookDeleteApiView.as_view()),
    path('books/update/<int:pk>/', BookUpdateApiView.as_view()),
]