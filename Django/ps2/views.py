from django.shortcuts import render
from .forms import Registration_form, Retrieval_form
from .models import Users, Artists, Ratings, SongAttributes
# Create your views here.

def Registration(request):
    registration_form = Registration_form
    retrieval_form = Retrieval_form
    if request.method == 'POST':
        form = Registration_form(request.POST)
    if form.is_valid():
        try:
            user = Users.object.get(username = form.cleaned_data.get("username"))

def Song_Retrieval(request):
    registration_form = Registration_form
    retrieval_form = Retrieval_form
    if request.method == 'POST':
        form = Retrieval_form(request.POST)
    if form.is_valid():
        try: 
            ratings = Ratings.objects.filter(username=form.cleaned_data.get("username"))