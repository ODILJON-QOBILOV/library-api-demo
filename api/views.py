from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book
from .serializers import BookSerializer

from rest_framework import generics, status


# Create your views here.


# GENERICS VIEW

# class BookViewApi(generics.ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#
# class BookDetailApiView(generics.RetrieveUpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
# class BookCreateApiView(generics.CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#
# class BookDeleteApiView(generics.RetrieveDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
# class BookUpdateApiView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


# APIView

class BookListApiView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer_data = BookSerializer(books, many=True).data
        data = {
            'books': serializer_data
        }
        return Response(data)


class BookCreateApiView(APIView):
    def post(self, request):
        data = request.data
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'status': status.HTTP_201_CREATED,
                'books': data
            }
            return Response(data)
        else:
            return Response({
                'message': 'Serializer is not valid'
            })


class BookDetailApiView(APIView):
    def get(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            serializer_data = BookSerializer(book).data
            data = {
                'status': status.HTTP_200_OK,
                'book': serializer_data
            }
            return Response(data)
        except Exception:
            data = {
                'status': status.HTTP_404_NOT_FOUND,
                'message': "Book Doesn't exists"
            }
            return Response(data)


class BookDeleteApiView(APIView):
    def delete(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            book.delete()
            return Response({
                'status': 'Succesfully deleted'
            })
        except Exception:
            return Response({
                'status': status.HTTP_404_NOT_FOUND,
                'message': 'Book is not found'
            })


class BookUpdateApiView(APIView):
    def put(self, request, pk):
        book = get_object_or_404(Book.objects.all(), id=pk)
        data = request.data
        serializer = BookSerializer(instance=book, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            book_saved = serializer.save()
        return Response({
            'status': True,
            'message': f'Book {book_saved} updated'
        })
