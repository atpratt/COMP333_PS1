from django.shortcuts import render
from .forms import Registration_form, Song_Retrieval_form
from .models import 
# Create your views here.

def Registration(request):
    registration_form = Registration_form
    retrieval_form = Song_Retrieval_form
    if request.method == 'POST':
        form = Registration_form(request.POST)
    if form.is_valid():
        try:
            user = Users.object.get(username = form.cleaned_data.get("username"))

def Song_Retrieval(request):
    registration_form = Registration_form
    retrieval_form = Song_Retrieval_form
    if request.method == 'POST':
        form = Song_Retrieval_form(request.POST)
    if form.is_valid():
        try: 
            ratings = Ratings.objects.filter(username=form.cleaned_data.get("username"))