from django.urls import path
from .views import  api, detail, category, ArticleListView

app_name = 'blog'
urlpatterns = [
    path('api/', api, name='api'),
    path('home/', ArticleListView.as_view(), name='home'),
    path('home/<int:page>/', ArticleListView.as_view(), name='home'),
    path('article/<slug:slug>', detail, name='detail'),
    path('category/<slug:slug>', category, name='category'),
    path('category/<slug:slug>/<int:page>/', category, name='category'),

]
