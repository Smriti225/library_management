from django.shortcuts import render
from rest_framework import viewsets
from  .models import Book
from .Bookserializer import BookSerializer
from  rest_framework_simplejwt.authentication import JWTAuthentication 
from rest_framework.permissions import IsAuthenticated


class Books(viewsets.ReadOnlyModelViewSet):
    queryset=Book.objects.all()
    serializer_class= BookSerializer
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]