from django.conf.urls import patterns, url

from mixtape import views

urlpatterns = patterns('',
                       url(r'^$', views.MixTapeList.as_view()),
                       url(r'^(?P<pk>\d+)/$', views.mixtape, name='mixtape'),
                       url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'mixtape/login.html'}, name='login'),
                       url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', name='logout'),
                       url(r'^upload/$', views.upload, name='upload'),
                       url(r'^mixes', views.UserMixTapeList.as_view(), name='user_mixes'),
                       url(r'^add-favorite/(?P<pk>\d+)/$', views.add_favorite, name='favorite'),
                       url(r'^favorites', views.FavoriteMixTapeList.as_view(), name='favorite_mixes'),
                       )
