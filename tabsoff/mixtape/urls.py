from django.conf.urls import patterns, url

from mixtape import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^(?P<pk>\d+)/$', views.mixtape, name='mixtape'),
                       url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'mixtape/login.html'}, name='login'),
                       url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', name='logout'),
                       )
