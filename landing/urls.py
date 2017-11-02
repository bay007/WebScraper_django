from django.conf.urls import url
from .views import index, characters

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^characters/$', characters, name="characters"),
    url(r'^characters/(?P<page>\d+)/$', characters, name="characters")
]
