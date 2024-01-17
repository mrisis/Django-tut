from django.contrib.auth import views
from .views import ArticleListView
from django.urls import path

app_name = 'accounts'
urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
]

urlpatterns += [
    path('home/', ArticleListView.as_view(), name='home'),
]
