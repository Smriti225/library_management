from .models import Book
from rest_framework import serializers
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields=['bookid','book_title','book_Desc','author_name','published_date']

