from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Article

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


def home(request):
    context = {
        'articles': Article.objects.filter(status='p')

    }
    return render(request, 'blog/home.html', context)


def detail(request, slug):
    context = {
        'article': get_object_or_404(Article, slug=slug)
    }
    return render(request, 'blog/single.html', context)


