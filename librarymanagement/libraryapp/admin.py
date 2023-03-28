from django.contrib import admin
from .models import CustomUser
from .models import Book
# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display=['email','mobile','address','pincode','first_name','last_name']

print("hi")
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=['bookid','book_title','book_Desc','author_name','published_date']