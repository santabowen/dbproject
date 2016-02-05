from django.conf.urls import include, url
from django.contrib import admin

from . import views

app_name = 'dbproject'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^impcsv/$', views.impcsv, name='impcsv'),
    url(r'^singlequery/$', views.singlequery, name='singlequery'),
    url(r'^customquery/$', views.customquery, name='customquery'),
    url(r'^prediction/$', views.prediction, name='prediction'),
]