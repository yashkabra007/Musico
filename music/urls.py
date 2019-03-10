from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    # /music/
    url(r'^$', views.index, name='index'),
    # /music/22/
    url(r'^(?P<album_id>[0-9]+)/$', views.details, name='details'),
    # /music/22/favorite/
    url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),

]
