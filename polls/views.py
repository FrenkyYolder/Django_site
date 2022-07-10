# views.py
from django.http import HttpResponse


def main_page(request):
    print('Юзер на сайте')
    return HttpResponse('Привет!')
