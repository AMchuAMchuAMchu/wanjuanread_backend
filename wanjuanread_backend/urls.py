"""wanjuanread_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# 如何引入别的views的同时可以保证不混乱...(起别名)
from like import views as like_views
from user import views as user_views

urlpatterns = [
    path(r'likeData/',like_views.likeData),
    path(r'allBooks/',like_views.allBooks),
    path(r'userRegister/',user_views.userRegister),
    path(r'login/',user_views.login),
]
