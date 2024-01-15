from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from .models import Article, Category
from django.views.generic import ListView, DetailView


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


# def home(request, page=1):
#     articles = Article.objects.published()
#     paginator = Paginator(articles, 2)
#     articles = paginator.get_page(page)
#     context = {
#         'articles': articles,
#         'category': Category.objects.filter(status=True)
#
#     }
#     return render(request, 'blog/home.html', context)

class ArticleListView(ListView):

    queryset = Article.objects.published()
    paginate_by = 2
    context_object_name = "articles"
    template_name = "blog/home.html"


# def detail(request, slug):
#     context = {
#         'article': get_object_or_404(Article, slug=slug)
#     }
#     return render(request, 'blog/article_detail.html', context)

class ArticleDetail(DetailView):
    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Article.objects.published(), slug=slug)


def category(request, slug, page=1):
    category = get_object_or_404(Category, slug=slug, status=True)
    articles_list = category.articles.published()
    paginator = Paginator(articles_list, 2)
    articles = paginator.get_page(page)
    context = {
        'category': category,
        'articles': articles,
    }
    return render(request, 'blog/category.html', context)


