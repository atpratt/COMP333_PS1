from django.db import models

class Users(models.Model):
    username = models.CharField(max_length = 255, primary_key = True)
    password = models.CharField(max_length = 255)

class SongAttributes(models.Model):
    song = models.CharField(max_length = 255, primary_key = True)
    artist = models.CharField(max_length = 255)
    album = models.CharField(max_length = 255)
    genre = models.CharField(max_length = 255)
    year = models.IntegerField(max_digits=4, default = 2000)
    record_company = models.CharField(max_length = 255)

       def __str__(self):
        return (self.song
                + "" + self.artist 
                + "" + self.album
                + "" + self.genre
                + "" + self.year
                + "" + self.record_company)

class Artists(models.Model):
    song = models.ForeignKey(SongAttributes, max_length = 255, primary_key = True, on_delete=models.CASCADE)
    artist = models.ForeignKey(SongAttributes, max_length = 255)

class Ratings(models.Model):
    username = models.ForeignKey(Users, max_length = 255, primary_key = True, on_delete=models.CASCADE)
    song = models.ForeignKey(Artists, max_length = 255, on_delete=models.CASCADE)
    rating = models.IntegerField()



 
    

#unique = true marks them as the primary key
#cascade deletes them from other tables too when deleted from their own
#changed unique to primary key
#added foreign keys




#We need to ad the ps2 file to the settings
#In order to create the tables/SQl queries we need to run these in the terminal
#python3 manage.py makemigrations
#python3 manage.py migrate 