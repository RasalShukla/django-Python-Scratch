from django.conf.urls import url
from . import views

# ^ starts with $ ends with nothing i.e. /posts/


urlpatterns = [
    url(r'^$', views.index, name ='index'),
    url(r'^details/(?P<id>\d+)/$', views.details, name ='details')
];