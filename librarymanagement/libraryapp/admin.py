from django.contrib import admin
from .models import CustomUser
from .models import Book
# Register your models here.


# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("email", "is_staff", "is_active",)
    list_filter = ("email", "is_staff", "is_active",)
    fieldsets = (
        ("Account Details", {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "user_permissions")}),
        ("Profile Details", {"fields": ("mobile","pincode","address")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "username","email", "password1", "password2", "is_staff",
                "is_active", "user_permissions","mobile","pincode","address"
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(CustomUser, CustomUserAdmin)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=['book_title','book_Desc','author_name','published_date']