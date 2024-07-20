from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book
from .serializers import BookSerializer

from rest_framework import generics

# Create your views here.


class BookViewApi(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# class BookViewApi(APIView):
#     def get(self, request):
#         books = Book.objects.all()
#         serializer_data = BookSerializer(books, many=True).data
#         data = {
#             "data": serializer_data
#         }
#         return Response(data)

class BookDetailApiView(generics.RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookCreateApiView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# class BookCreateApiView(APIView):
#     def post(self, request):
#         data = request.data
#         serializer = BookSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             data = {
#                 'status': 200,
#                 'books': data
#             }
#             return Response(data)

class BookDeleteApiView(generics.RetrieveDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookUpdateApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer