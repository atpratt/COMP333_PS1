from django.contrib import admin

# Register your models here.
from .models import users
@admin.register(users)
class usersAdmin(admin.ModelAdmin):
    list_display = ("username",)
    search_feilds = ("username",)