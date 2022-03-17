from django.shortcuts import get_object_or_404, render
from .forms import Registration_form, Retrieval_form
from .models import User, Artist, Rating, Attribute
# Create your views here.

#Query the users table
def Registration(request):
    try:
        usern=request.POST['username']
        if usern == "": #no user inputed
            message = "No information"
            context = {'message' : message, 'user' : ''}
            return render(request, 'app/detail.html', context)
        pswd = request.POST['password']
        if User.objects.filter(username=usern).count()==1: 
            #there already exists a user with this name
            message = "This Username has been taken"
            context = {'message' : message, 'user' : ''}
            return render(request, 'app/detail.html', context)
        
        #creates the user and saves to DB
        u = User(username=usern, password=pswd)
        u.save()

        message = "New User Created"
        context = {'message' : message, 'user' : ''}
        return render(request, 'app/detail.html', context)

    except(KeyError):
        message = "Not Availible"
        context = {'message' : message, 'user' : ''}
        return render(request, 'app/detail.html', context)


# def Registration(request):
#     registration_form = Registration_form
#     retrieval_form = Retrieval_form
#     if request.method == 'POST':
#         form = Registration_form(request.POST)
#         if form.is_valid():
#             try:
#                 user = User.objects.get(username = form.cleaned_data.get("username"))
#             except User.DoesNotExist:
#                 user = None
            
#             #if username already in db
#             if (user != None):
#                 registration_form.output = "The username '" + form.cleaned_data.get("username") + "' has already been taken.  Please choose a different username."
            
#             #if username not in db
#             if (form.cleaned_data.get("username") != "" and user == None):
#                 new_user = User.objects.get(username = form.cleaned_data.get("username"))
#                 new_user.save()
#                 registration_form.output = "Successfully registered " + form.cleaned_data.get("username") + "!"
            
#             #if either username or password left blank
#             if (form.cleaned_data.get("username") == "" or form.cleaned_data.get("password") == ""):
#                 registration_form.output = "You'll need to enter both a username and password!"
        
#             context = {'registration_form': registration_form, 'retrieval_form': retrieval_form}

#         else:
#             context = {'registration_form': registration_form, 'retrieval_form': retrieval_form}
        
#     return render(request, 'app/detail.html', context)
    
    # output = " "
    # if form.is_valid():
    #     username = form.cleaned_data.get("username")
    #     password = form.cleaned_data.get("password")
    #     try:
    #         User.objects.get(username = username)
    #         output = "That username has already been taken.  Please choose a different username."
    #     except:
    #         if username == "" or password == "":
    #             output = "You'll need to enter both a username and password!"
    #         else:
    #             User.objects.create(username=username, password=password)
    #             output = "Successfully registered user."

    # return output
  

#Query the ratings table
# def Ratings_Retrieval(request):
#     registration_form = Registration_form
#     retrieval_form = Retrieval_form
#     if request.method == 'POST':
#         form = Retrieval_form(request.POST)
#         if form.is_valid():
#             try: 
#                 #This may be the bug. Do we use "input" from forms.py or what is in models.py?
#                 ratings = Rating.objects.filter(username=form.cleaned_data.get("input"))
#                 #retrieval_form.output = ""
#                 context = {'registration_form': registration_form, 'retrieval_form': retrieval_form, 'ratings': ratings}
#             except Rating.DoesNotExist:
#                 #retrieval_form.output = ""
#                 context = {'registration_form': registration_form, 'retrieval_form': retrieval_form}
#         else:
#             #retrieval_form.output = ""
#             context = {'registration_form': registration_form, 'retrieval_form': retrieval_form}
#     else:
#         #retrieval_form.output = ""
#         context = {'registration_form': registration_form, 'retrieval_form': retrieval_form}
    
#     return render(request, 'app/detail.html', context)



def Ratings_Retrieval(request):
    try:
        #song_req=request.POST['song']
        #rating_req=request.POST['rating']
        usern=request.POST['username']

        #If there exists a user with that username
        if User.objects.filter(username=usern).count()==1: 
            rated_songs = Rating.objects.filter(username=usern)

            #Has the user has  rated any songs?
            if rated_songs.count() == 0:
                #there are no songs that have been rated by this user
                message = "This user has not rated any songs"
                context = {'message' : message, 'user' : usern}
                return render(request, 'app/detail.html', context)
                ######I THINK WE NEED A NEW HTML FILE TO REPORT THE RETREVIAL
            
            else:
                #the user has rated 1+ song for us to return/show to the user in the HTML
                context = {'rated_songs' : rated_songs, 'Username' : usern}
                return render(request, 'app/detail.html', context)

    except(KeyError):
        message = "Not Availible"
        context = {'message' : message, 'user' : ''}
        return render(request, 'app/detail.html', context)



def Attributes_Retrieval(request):
    try:
        name =request.POST['artist_name']

        if Attribute.objects.filter(name).count()==1:
            #there is an artist for this retrival
            their_album =request.POST['album']
            the_genre =request.POST['genre']
            the_year =request.POST['year']
            the_record_company =request.POST['record_company']

            context = {'album' : their_album, 'genre' : the_genre, 'year' : the_year, "record_company" : the_record_company }
            return render(request, 'app/detail.html', context)

    
    except(KeyError):
        message = "Not Availible for that Artist"
        context = {'message' : message, 'artist_name' : ''}
        return render(request, 'app/detail.html', context)



# def Attributes_Retrieval(request):
#     registration_form = Registration_form
#     retrieval_form = Retrieval_form
#     if request.method == 'POST':
#         form = Retrieval_form(request.POST)
#         if form.is_valid():
#             try: 
#                 #retrieval_form.output = ""
#                 #This may be the bug. Do we use "input" from forms.py or what is in models.py?
#                 attributes = Attribute.objects.filter(name=form.cleaned_data.get("input"))
#                 context = {'registration_form': registration_form, 'retrieval_form': retrieval_form, 'attributes': attributes}
#             except Attribute.DoesNotExist:
#                 #retrieval_form.output = ""
#                 context = {'registration_form': registration_form, 'retrieval_form': retrieval_form}
#         else:
#             #retrieval_form.output = ""
#             context = {'registration_form': registration_form, 'retrieval_form': retrieval_form}
#     else:
#         #retrieval_form.output = ""
#         context = {'registration_form': registration_form, 'retrieval_form': retrieval_form}

#     return render(request, 'app/detail.html', context)



def index(request):
    registration_form = Registration_form
    retrieval_form = Retrieval_form
    context = {'registration_form': registration_form, 'retrieval_form': retrieval_form}
    return render(request, "app/detail.html", context)