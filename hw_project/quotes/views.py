from bson import ObjectId
from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from .utils import get_mongodb
from .models import Author, Quote, Tag


def main(request, page=1):
    db = get_mongodb()
    quotes = db.quotes.find()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, 'quotes/index.html', context={'quotes': quotes_on_page})


def author(request, id_):
    db = get_mongodb()
    author_info = db.authors.find_one({'_id': ObjectId(id_)})
    return render(request, 'quotes/author.html', context={'author': author_info})
