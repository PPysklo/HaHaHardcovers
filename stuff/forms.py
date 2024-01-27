from django.forms import ModelForm
from django import forms
from .models import Books, Review

class BookForm(ModelForm):
    class Meta:
        model = Books
        fields = ['author','title', 'description', 'price']
        
        widgets = {
            'tags' : forms.CheckboxSelectMultiple(),
            'description': forms.Textarea(attrs={'rows':7, 'cols':53})
        }
    
    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args,**kwargs)
        
        # self.fields['title'].widget.attrs.update({'class':'input',})
        for name,field  in self.fields.items():
            field.widget.attrs.update({'class' : "bookFormField"})

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'body']

        labels = {
            'value': 'Postaw ocenę',
            'body': 'Dodaj komentarz do oceny'
        }