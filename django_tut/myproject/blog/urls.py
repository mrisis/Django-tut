from django.urls import path
from .views import home, api, articles, detail

app_name = 'blog'
urlpatterns = [
    path('home/', home, name='home'),
    path('api/', api, name='api'),
    path('articles/', articles, name='articles'),
    path('article/<slug:slug>', detail, name='detail'),

]
