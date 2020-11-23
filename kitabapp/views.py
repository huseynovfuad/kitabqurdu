from django.shortcuts import render,redirect
from .utils import get_html_alinino,get_html_kitabim
from .models import Book
# Create your views here.


def home(request):
    context = {}
    if 'book' in request.GET:
        book = request.GET.get('book')
        getlist = get_html_alinino(book) + get_html_kitabim(book)
        context['books'] = getlist
    return render(request,'home/home.html',context)

