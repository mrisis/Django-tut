from django.urls import path
from .views import home, api, home, detail, category

app_name = 'blog'
urlpatterns = [
    path('api/', api, name='api'),
    path('home/', home, name='home'),
    path('home/<int:page>/', home, name='home'),
    path('article/<slug:slug>', detail, name='detail'),
    path('category/<slug:slug>', category, name='category'),
    path('category/<slug:slug>/<int:page>/', category, name='category'),

]
