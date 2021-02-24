from django.contrib import admin

from .models import Category, Genre, Title, User


class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "role")


class TitleAdmin(admin.ModelAdmin):
    list_display = ("name", "year", "description", "category")


class GenreAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")


admin.site.register(User, UserAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Category, CategoryAdmin)
