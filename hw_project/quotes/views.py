from bson import ObjectId
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from django.shortcuts import render, redirect

from .utils import get_mongodb
from .models import Author, Quote, Tag
from .forms import AddAuthor, AddForm


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


def find_tag(request, tag_name):
    tag = Tag.objects.get(name=tag_name)
    quotes = Quote.objects.filter(tags=tag)
    context = {
        'tag': tag,
        'quotes': quotes
    }
    return render(request, 'quotes/tags.html', context)


@login_required
def add_author(request):
    if request.method == 'POST':
        form = AddAuthor(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotes:root')
        else:
            return render(request, 'quotes/add_author.html', context={'form': form})

    return render(request, 'quotes/add_author.html', context={'form': AddAuthor()})


@login_required
def add_quote(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            new_quote = form.save(commit=False)
            new_quote.user = request.user
            new_quote.save()
            return redirect(to='quotes:root')
        else:
            return render(request, 'quotes/add_quote.html', context={'form': form})

    return render(request, 'quotes/add_quote.html', context={'form': AddAuthor()})
