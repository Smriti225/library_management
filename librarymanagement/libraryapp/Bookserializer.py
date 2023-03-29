from .models import Book
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    book_title=serializers.CharField(max_length=10)
    book_Desc=serializers.CharField(max_length=40)
    author_name=serializers.CharField(max_length=50)
    published_date=serializers.DateField()
    class Meta:
        model=Book
        fields='__all__'
  

    
    


    

