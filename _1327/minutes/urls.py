from django.conf.urls import url
from django.contrib import admin

from . import views

admin.autodiscover()

urlpatterns = [
	url(r"^$", views.list, name='list'),
	url(r"(?P<groupid>[\d]+)$", views.list, name='list'),
]
