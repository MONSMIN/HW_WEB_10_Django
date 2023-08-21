from django.forms import ModelForm, CharField, TextInput, Textarea
from .models import Author, Quote, Tag



class AddAuthor(ModelForm):
    fullname = CharField(max_length=40, min_length=5, widget=TextInput(attrs={'class': 'form-control'}))
    born_date = CharField(max_length=25, min_length=12, widget=TextInput(attrs={'class': 'form-control'}))
    born_location = CharField(max_length=150, min_length=12, widget=TextInput(attrs={'class': 'form-control'}))
    description = CharField(widget=Textarea(attrs={'class': 'form-control', 'size': 50}))

    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']


class AddForm(ModelForm):
    author = CharField(min_length=5, max_length=150, required=True, widget=TextInput(attrs={'class': 'form-control'}))
    quote = CharField(min_length=5, required=True, widget=Textarea(attrs={'class': 'form-control'}))
    tags = CharField(required=False, widget=TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Quote
        fields = ['quote', 'tags', 'author']
