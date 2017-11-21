
from django.conf.urls import url
from django.contrib import admin

from expenses import views
app_name = 'expenses'
urlpatterns = [
    url(r'^$', views.home, name='home'),
]
