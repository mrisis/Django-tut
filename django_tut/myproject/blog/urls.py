from django.urls import path
from .views import api, ArticleDetail, CategoryList, ArticleListView

app_name = 'blog'
urlpatterns = [
    path('api/', api, name='api'),
    path('home/', ArticleListView.as_view(), name='home'),
    path('home/<int:page>/', ArticleListView.as_view(), name='home'),
    path('article/<slug:slug>', ArticleDetail.as_view(), name='detail'),
    path('category/<slug:slug>', CategoryList.as_view(), name='category'),
    path('category/<slug:slug>/<int:page>/', CategoryList.as_view(), name='category'),

]
