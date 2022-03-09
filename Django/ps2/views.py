from django.shortcuts import render
from .forms import Registration_form, Retrieval_form
from .models import Users, Artists, Ratings, SongAttributes
# Create your views here.

#Query the users table
def Registration(request):
    registration_form = Registration_form
    retrieval_form = Retrieval_form
    if request.method == 'POST':
        form = Registration_form(request.POST)
        if form.is_valid():
            try:
                user = Users.object.get(username = form.cleaned_data.get("username"))
            except Users.DoesNotExist:
                user = None

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
    retrieval_form = Retrieval_form
    if request.method == 'POST':
        form = Retrieval_form(request.POST)
        if form.is_valid():
            try: 
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
                attributes = SongAttributes.objects.filter(name=form.cleaned_data.get("username"))
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