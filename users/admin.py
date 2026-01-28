# from django.contrib import admin
# from .models import User
# Register your models here.
# admin.site.register(User)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):

    ordering = ("id",)
    list_display = (
        "id",
        "name",
        "role",
        "email",
        "phone",
        "language",
        "location",
        "is_verified",
        "is_staff",
    )

    list_filter = ("role", "language", "is_verified", "is_staff")
    search_fields = ("id",)

    fieldsets = (
        (None, {"fields": ("phone", "password")}),
        ("Profile Info", {"fields": ("role", "language", "location")}),
        ("Verification", {"fields": ("is_verified",)}),
        ("Permissions", {
            "fields": (
                "is_active",
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions",
            )
        }),
        ("Important dates", {"fields": ("last_login",)}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "phone",
                "email",
                "password1",
                "password2",
                "role",
                "language",
                "location",
            ),
        }),
    )

