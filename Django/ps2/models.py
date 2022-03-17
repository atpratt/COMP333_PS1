from django.db import models

#Online it said that we need to add defaults to each element of the table
#Adding this removed some compiling errors in my terminal, but I am not 100% sure they are correct

class User(models.Model):
    username = models.CharField(max_length = 200, primary_key = True, default='SOME STRING')
    password = models.CharField(max_length = 200, default='SOME STRING')

class Attribute(models.Model):
    artist_name = models.CharField(max_length = 200, primary_key = True, default='SOME STRING')
    album = models.CharField(max_length = 200, default='SOME STRING')
    genre = models.CharField(max_length = 200, default='SOME STRING')
    year = models.IntegerField(default=2000)
    record_company = models.CharField(max_length = 200, default='SOME STRING')

    def __str__(self):
        return (self.artist_name
                + "" + self.album
                + "" + self.genre
                + "" + self.year
                + "" + self.record_company)

class Artist(models.Model):
    song = models.CharField(max_length = 200, primary_key = True, default='SOME STRING')
    artist = models.ForeignKey(Attribute, max_length = 200, on_delete=models.CASCADE, default='SOME STRING')

class Rating(models.Model):
    username = models.ForeignKey(User, max_length = 200, on_delete=models.CASCADE, default='SOME STRING')
    song = models.ForeignKey(Artist, max_length = 200, on_delete=models.CASCADE,default='SOME STRING')
    rating = models.IntegerField(default=2000)


#unique = true marks them as the primary key
#cascade deletes them from other tables too when deleted from their own
#changed unique to primary key
#added foreign keys




#We need to ad the ps2 file to the settings
#In order to create the tables/SQl queries we need to run these in the terminal
#python3 manage.py makemigrations
#python3 manage.py migrate 