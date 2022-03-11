from django.contrib import admin

# Register your models here.
from .models import Users
from .models import Attributes
from .models import Artists
from .models import Ratings

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ("username",)
    search_feilds = ("username",)

#based on slides we need to register all of the models
@admin.register(Attributes)
class AttributesAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(Artists)
class ArtistsAdmin(admin.ModelAdmin):
    list_display = ("song",)

@admin.register(Ratings)
class RatingsAdmin(admin.ModelAdmin):
    list_display = ("rating",)
    list_display = ("song_id",)
    list_display = ("username_id",)
