# views.py
from django.http import HttpResponse
from django.template import loader


def main_page(request):
    print('Юзер на сайте')
    templates = loader.get_template('main_page_1.html')
    context = {}
    rendered_page = templates.render(context, request)
    return HttpResponse(rendered_page)


def second_page(request):
    print('Юзер на второй странице')
    templates = loader.get_template('second_page.html')
    context = {}
    rendered_page = templates.render(context, request)
    return HttpResponse(rendered_page)
