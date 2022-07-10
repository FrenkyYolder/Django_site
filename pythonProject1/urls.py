from django.urls import path
from django.http import HttpResponse


def main_page(request):
    print('Юзер на сайте')
    return HttpResponse('Привет!')


urlpatterns = [
    path('', main_page),
]
