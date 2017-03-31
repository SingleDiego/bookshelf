"""bookshelf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from bookshelf_app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^add_book/', views.add_book, name='add_book'),
    url(r'^save_book/', views.save_book, name='save_book'),
    url(r'^book_list/', views.book_list, name='book_list'), 
    url(r'^clean_books_count/', views.clean_books_count, name='clean_books_count'), # 最近录入书目计数清零
    url(r'^book/(?P<id>\d+)$', views.book_detail, name='book_detail'), # 某本书的详情页面，id作为参数
]
