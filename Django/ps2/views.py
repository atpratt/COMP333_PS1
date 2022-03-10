from django.shortcuts import render
from .forms import Registration_form, Retrieval_form
from .models import Users, Artists, Ratings, SongAttributes
# Create your views here.

#Query the users table
def Registration(request):
    registration_form = Registration_form
    retrieval_form = Retrieval_form
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

    return output
    #         if (form.cleaned_data.get("username") != "" and user == None):
    #             new_user = Users(username = form.cleaned_data.get("username"), password = form.cleaned_data.get("password"))
    #             new_user.save()
    #             registration_form.output = "Successfully registered " + form.cleaned_data.get("username") + "!"
    #         elif (form.cleaned_data.get("username") == "" or form.cleaned_data.get("password") == ""):
    #             registration_form.output = "You'll need to enter both a username and password!"
    #             context = {'registration_form': registration_form, 'retrieval_form': retrieval_form}
    #         else:
    #             registration_form.output = "The username '" + form.cleaned_data.get("username") + "' has already been taken.  Please choose a different username."
    #             context = {'registration_form': registration_form, 'retrieval_form': retrieval_form}
    #     else:
    #         context = {'registration_form': registration_form, 'retrieval_form': retrieval_form}

    #return render(request, 'ps2/index.html', context)

#Query the ratings table
def Ratings_Retrieval(request):
    registration_form = Registration_form
    retrieval_form = Retrieval_form
    if request.method == 'POST':
        form = Retrieval_form(request.POST)
        if form.is_valid():
            try: 
                #This may be the bug. Do we use "input" from forms.py or what is in models.py?
                ratings = Ratings.objects.filter(username=form.cleaned_data.get("input"))
                #retrieval_form.output = ""
                context = {'registration_form': registration_form, 'retrieval_form': retrieval_form, 'ratings': ratings}
            except Ratings.DoesNotExist:
                #retrieval_form.output = ""
                context = {'registration_form': registration_form, 'retrieval_form': retrieval_form}
        else:
            #retrieval_form.output = ""
            context = {'registration_form': registration_form, 'retrieval_form': retrieval_form}
    
    return render(request, 'ps2/index.html', context)

#Query the song attribute table
#??????????????????????????????????
def Attributes_Retrieval(request):
    registration_form = Registration_form
    retrieval_form = Retrieval_form
    if request.method == 'POST':
        form = Retrieval_form(request.POST)
        if form.is_valid():
            try: 
                #retrieval_form.output = ""
                #This may be the bug. Do we use "input" from forms.py or what is in models.py?
                attributes = SongAttributes.objects.filter(song=form.cleaned_data.get("input"))
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

    return render(request, 'ps2/index.html', context)



def index(request):
    registration_form = Registration_form
    retrieval_form = Retrieval_form
    context = {'registration_form': registration_form, 'retrieval_form': retrieval_form}
    return render(request, "ps2/index.html", context)