from django.urls import path
from .views import home, api, home, detail

app_name = 'blog'
urlpatterns = [
    path('api/', api, name='api'),
    path('home/', home, name='articles'),
    path('article/<slug:slug>', detail, name='detail'),

]
