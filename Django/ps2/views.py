from django.shortcuts import render
from .forms import Registration_form, Retrieve_rating_form, Retrieve_attributes_form
from .models import Users, Artists, Ratings, SongAttributes
# Create your views here.

#Query the users table
def Registration(request):
    form = Registration_form(request.POST)
    output = " "
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        try:
            Users.object.get(username = username)
            output = "That username has already been taken.  Please choose a different username."
        except:
            if username == "" or password == "":
                output = "You'll need to enter both a username and password!"
            else:
                Users.objects.create(username=username, password=password)
                output = "Successfully registered user."


            if (form.cleaned_data.get("username") != "" and user == None):
                new_user = Users(username = form.cleaned_data.get("username"), password = form.cleaned_data.get("password"))
                new_user.save()
                registration_form.output = "Successfully registered " + form.cleaned_data.get("username") + "!"
            elif (form.cleaned_data.get("username") == "" or form.cleaned_data.get("password") == ""):
                registration_form.output = "You'll need to enter both a username and password!"
                context = {'registration_form': registration_form, 'retrieval_form': retrieval_form}
            else:
                registration_form.output = "The username '" + form.cleaned_data.get("username") + "' has already been taken.  Please choose a different username."
                context = {'registration_form': registration_form, 'retrieval_form': retrieval_form}
        else:
            context = {'registration_form': registration_form, 'retrieval_form': retrieval_form}

    return render(request, 'music-db/index.html', context)

#Query the ratings table
def Ratings_Retrieval(request):
    registration_form = Registration_form
    retrieval_form = Retrieve_rating_form
    if request.method == 'POST':
        form = Retrieve_rating_form(request.POST)
        if form.is_valid():
            try: 
                #This may be the bug. Do we use "input" from forms.py or what is in models.py?
                ratings = Ratings.objects.filter(username=form.cleaned_data.get("username"))
                #retrieval_form.output = ""
                context = {'registration_form': registration_form, 'retrieval_form': retrieval_form, 'ratings': ratings}
            except Ratings.DoesNotExist:
                #retrieval_form.output = ""
                context = {'registration_form': registration_form, 'retrieval_form': retrieval_form}
        else:
            #retrieval_form.output = ""
            context = {'registration_form': registration_form, 'retrieval_form': retrieval_form}
    
    return render(request, 'music-db/index.html', context)

#Query the song attribute table
def Attribute_Retrieval(request):
    registration_form = Registration_form
    retrieval_form = Retrieval_form
    if request.method == 'POST':
        form = Retrieval_form(request.POST)
        if form.is_valid():
            try: 
                #retrieval_form.output = ""
                #This may be the bug. Do we use "input" from forms.py or what is in models.py?
                attributes = SongAttributes.objects.filter(input=form.cleaned_data.get("input"))
                context = {'registration_form': registration_form, 'retrieval_form': retrieval_form, 'attributes': attributes}
            except SongAttributes.DoesNotExist:
                #retrieval_form.output = ""
                context = {'registration_form': registration_form, 'retrieval_form': retrieval_form}
        else:
            #retrieval_form.output = ""
            context = {'registration_form': registration_form, 'retrieval_form': retrieval_form}
    else:
        #retrieval_form.output = ""
        context = {'registration_form': registration_form, 'retrieval_form': retrieval_form}

    return render(request, 'music-db/index.html', context)

def index(request):
    registration_form = Registration_Form
    retrieval_form = Retrieval_Form
    context = {'registration_form': registration_form, 'retrieval_form': retrieval_form}
    return render(request, "music-db/index.html", context)