from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework import permissions, status
from django.shortcuts import get_object_or_404 
from .models import Book
from .serializers import BookSerizalier
# Create your views here.

class BookListView(APIView):

    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerizalier(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BookSerizalier(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetailView(APIView):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerizalier(book)
        return Response(serializer.data)
    
    def put(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerizalier(book, data=request.data)  # Truyền đối tượng book vào serializer
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)