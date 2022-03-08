from django.db import models

class artists(models.Model):
    artist = models.CharField(max_length=100, unique=True)
    song = models.CharField(max_length=100)

#unique = true marks them as the primary key
#cascade deletes them from other tables too when deleted from their own
class raitings(models.Model):
    username = models.CharField(max_length=100, unique=True)
    rating = models.CharField(max_length=100)
    song = models.CharField(max_length=100)

class users(models.Model):
    username = models.ForeignKey(raitings, on_delete=models.CASCADE)
    password = models.CharField(max_length=100)

#We need to ad the ps2 file to the settings
#In order to create the tables/SQl queries we need to run these in the terminal
#python3 manage.py makemigrations
#python3 manage.py migrate 