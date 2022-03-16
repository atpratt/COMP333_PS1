from django.contrib import admin

# Register your models here.
from .models import User
from .models import Attribute
from .models import Artist
from .models import Rating

@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    list_display = ("username",)
    search_feilds = ("username",)

#based on slides we need to register all of the models
@admin.register(Attribute)
class AttributesAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(Artist)
class ArtistsAdmin(admin.ModelAdmin):
    list_display = ("song",)

@admin.register(Rating)
class RatingsAdmin(admin.ModelAdmin):
    list_display = ("rating",)
    list_display = ("song_id",)
    list_display = ("username_id",)
