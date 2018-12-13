from django.urls import path
from django.conf.urls import include, url
from django.contrib import admin
from . import views


urlpatterns = [
    path('login', views.login, name='login'),
    path('articles', views.articles , name = 'articles'),
    path('news', views.news, name = 'news'),
    path('handlecreatearticles', views.handlecreatearticles , name="handlecreatearticles"),
    path('createart',views.createarticles, name="createart"),
    path('sourcepage', views.sourcepage),
    ]
