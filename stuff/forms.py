from django.forms import ModelForm
from django import forms
from .models import Books, Review

class BookForm(ModelForm):
    class Meta:
        model = Books
        fields = ['author','title', 'description' , 'price']
        
        widgets = {
            'tags' : forms.CheckboxSelectMultiple(),
        }

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'body']

        labels = {
            'value': 'Postaw ocenę',
            'body': 'Dodaj komentarz do oceny'
        }