from rest_framework import serializers
from .models import Book

class BookSerizalier(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'author', 'published_date')