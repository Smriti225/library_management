from django.shortcuts import render
from .models import Book
from .Bookserializer import BookSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    authentication_classes=[]
    permission_classes=[IsAdminUser]