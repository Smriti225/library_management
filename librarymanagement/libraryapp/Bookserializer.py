from .models import Book,CustomUser
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
class BookSerializer(serializers.ModelSerializer):
    book_title=serializers.CharField(max_length=20)
    book_Desc=serializers.CharField(max_length=50)
    author_name=serializers.CharField(max_length=10)
    published_date=serializers.DateField()
    class Meta:
        model=Book
        fields="__all__"

class UserSerializer(serializers.ModelSerializer):
    def validate_password(self,password):
        password=make_password(password)
        return password
    class Meta:
        model=CustomUser
        fields="__all__"


