import requests
from bs4 import BeautifulSoup
import urllib.request
import random
from .models import Book


def get_html_alinino(book):
    try:
        textlists = []
        main_link = 'https://alinino.az'
        book = book.replace(" ","+")
        html_content = requests.get('https://alinino.az/search?q={book_name}'.format(book_name=book))
        soup = BeautifulSoup(html_content.text,'html.parser')
        for abc in soup.find_all('img', attrs={'class': 'product-card-image'}):
            title = abc.find_parent('div').find_next_sibling('div').select('.product-link')[0].text
            price = abc.find_parent('div').find_next_sibling('div').find_next_sibling('div').find_next_sibling('div').find_next_sibling('div').select('.in-card')[0].contents[0].strip()
            detail_url = main_link + abc.find_parent('div').find_next_sibling('div').select('.product-link')[0].get('href')
            image_url = abc.get('src')
            if Book.objects.filter(detail_url=detail_url).exists():
                book = Book.objects.get(detail_url=detail_url)
                book.price = price
                book.save()
                textlists.append(book)
            else:
                book = Book.objects.create(title=title, price=price, detail_url=detail_url, image_url=image_url)
                textlists.append(book)
        return textlists
    except:
        return 'tapilmadi'


def get_html_kitabim(book):
    try:
        textlists = []
        main_link = 'https://kitabim.az'
        book = book.replace(" ","+")
        html_content = requests.get('https://kitabim.az/index.php?category_id=0&search={book_name}&submit_search=&route=product%2Fsearch'.format(book_name=book))
        soup = BeautifulSoup(html_content.text,'html.parser')
        for abc in soup.find_all('img', attrs={'class': 'img-1'}):
            title = abc.find_parent('div').find_parent('div').find_next_sibling('div').select('h4')[0].select('a')[0].text
            detail_url = main_link + abc.find_parent('div').find_parent('div').find_next_sibling('div').select('h4')[0].select('a')[0].get('href')
            price = abc.find_parent('div').find_parent('div').find_next_sibling('div').select('.price-new')[0].text.strip()
            image_url = abc.get('src').strip()
            if Book.objects.filter(detail_url=detail_url).exists():
                book = Book.objects.get(detail_url=detail_url)
                book.price = price
                book.save()
                textlists.append(book)
            else:
                book = Book.objects.create(title=title, price=price, detail_url=detail_url, image_url=image_url)
                textlists.append(book)
        return textlists
    except:
        return 'tapilmadi'




