from django.urls import path
from .views import home, api, articles

urlpatterns = [
    path('home/', home, name='home'),
    path('api/', api, name='api'),
    path('articles/', articles, name='articles'),
]
