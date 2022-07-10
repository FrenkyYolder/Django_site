# views.py
from django.http import HttpResponse
from django.template import loader


def main_page(request):
    print('Юзер на сайте')
    html_page = loader.get_template('main_page_1.html')
    context = {}
    rendered_page = html_page.render(context, request)
    return HttpResponse(rendered_page)
