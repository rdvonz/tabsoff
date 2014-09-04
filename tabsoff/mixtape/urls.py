from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required, permission_required
from mixtape import views

urlpatterns = patterns('',
                       url(r'^$', views.MixTapeList.as_view()),
                       url(r'^(?P<pk>\d+)/$', views.MixTapeDetail.as_view(), name='mixtape'),
                       url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'mixtape/login.html'}, name='login'),
                       url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', name='logout'),
                       url(r'^upload/$', views.upload, name='upload'),
                       url(r'^mixes', login_required(views.UserMixTapeList.as_view()), name='user_mixes'),
                       url(r'^add-favorite/(?P<pk>\d+)/$', views.add_favorite, name='favorite'),
                       url(r'^favorites', login_required(views.FavoriteMixTapeList.as_view()), name='favorite_mixes'),
                       )
