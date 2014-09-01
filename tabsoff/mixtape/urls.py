from django.conf.urls import patterns, url

from mixtape import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^(?P<pk>\d+)/$', views.mixtape, name='mixtape')
                       )
