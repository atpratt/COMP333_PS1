from django import forms

class Registration_form(forms.Form):
    username = forms.CharField(label="New Username: ", max_length=255)
    password = forms.CharField(label="New Password: ", max_length=255)
    output = ""

class Song_Retrieval_form(forms.Form):
    username = forms.CharField(label="Rater's Username: ", max_length=255)