"""Assignmentproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from Assignmentapp import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^song/?$', views.song, name='song'),
    url(r'^add/song/?$', views.add_song, name='add_song'),
    url(r'^edit/song/(\d{1,6})/?$', views.edit_song, name='edit_song'),
    url(r'^delete/song/(\d{1,6})/?$', views.delete_song, name='delete_song'),
    url(r'^artist/?$', views.artist, name='artist'),
    url(r'^add/artist/?$', views.add_artist, name='add_artist'),
    url(r'^edit/artist/(\d{1,6})/?$', views.edit_artist, name='edit_artist'),
    url(r'^delete/artist/(\d{1,6})/?$', views.delete_artist, name='delete_artist'),
    url(r'^producer/?$', views.producer, name='producer'),
    url(r'^add/producer/?$', views.add_producer, name='add_producer'),
    url(r'^edit/producer/(\d{1,6})/?$', views.edit_producer, name='edit_producer'),
    url(r'^delete/producer/(\d{1,6})/?$', views.delete_producer, name='delete_producer'),
]
