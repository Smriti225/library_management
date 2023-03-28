from django.shortcuts import render
from rest_framework import viewsets
from  .models import Book
from .Bookserializer import BookSerializer
from  rest_framework_simplejwt.authentication import JWTAuthentication 
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from rest_framework import status
class Curdauth(viewsets.ViewSet):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAdminUser]

    def list(self,request):
        stu=Book.objects.all()
        serializer =BookSerializer(stu,many=True)
        return Response(serializer.data)
    
    def retrieve(self,request,pk=None):
        stu=Book.objects.filter(pk=pk).first()
        if stu is None:
             return Response({"msg":"book id not exist is not exist"},status=status.HTTP_404_NOT_FOUND)
        serializer=BookSerializer(stu)
        return Response(serializer.data)

    def create(self,request):
        serializer=BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"data created"},status=status.HTTP_201_CREATED)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk=None):
            stu=Book.objects.filter(pk=pk).first()
            if stu is None:
                 return Response({"msg":"book id not exist is not exist"},status=status.HTTP_404_NOT_FOUND)
            Serializer=BookSerializer(stu,data=request.data)
            if Serializer.is_valid():
                 Serializer.save()
                 return Response({"msg":"data updated"})
            return Response(Serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def partial_updata(self,request,pk=None):
         stu=Book.objects.filter(pk=pk).first()
         if stu is None:
                 return Response({"msg":"book id not exist is not exist"},status=status.HTTP_404_NOT_FOUND)
         serializer=BookSerializer(stu,data=request.data,partial=True)
         if serializer.is_valid():
              serializer.save()
              return Response({"msg":"data partailly updated"})
         
         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self,request,pk=None):

         stu=Book.objects.filter(pk=pk).first()
         if stu is None:
                return Response({"msg":"book id not exist is not exist"},status=status.HTTP_404_NOT_FOUND)
         stu.delete()
         return Response({"msg":"data deleted"})

class Books(viewsets.ReadOnlyModelViewSet):
    queryset=Book.objects.all()
    serializer_class= BookSerializer
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]