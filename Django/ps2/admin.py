from django.contrib import admin

# Register your models here.
from .models import Users
@admin.register(Users)
class usersAdmin(admin.ModelAdmin):
    list_display = ("username",)
    search_feilds = ("username",)