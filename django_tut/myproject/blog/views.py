from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Article


def home(request):
    return HttpResponse('hello reza>....')

def api(request):
    data = {
            "1": {
                'name': 'reza',
                'family': 'amin',
                'age': 23
            },
            "2": {
                'name': 'ali',
                'family': 'rezaei',
                'age': 23
            },

    }
    return JsonResponse(data)


def articles(request):
    context = {
        'articles': Article.objects.filter(status='p')

    }
    return render(request, 'blog/article.html', context)


