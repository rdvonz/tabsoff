from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from mixtape import views

urlpatterns = patterns('',
                       url(r'^$', views.MixTapeList.as_view(), name='index'),
                       url(r'^(?P<pk>\d+)/$', views.MixTapeDetail.as_view(), name='mixtape'),
                       url(r'^login/$', views.anywhere_login, name='login'),
                       url(r'^logout/$', views.anywhere_logout, name='logout'),
                       url(r'^upload/$', views.upload, name='upload'),
                       url(r'^login-required', views.not_logged_in, name='login_required'),
                       url(r'^mixes', login_required(views.UserMixTapeList.as_view()), name='user_mixes'),
                       url(r'^add-favorite/(?P<pk>\d+)/$', views.add_favorite, name='favorite'),
                       url(r'^favorites', login_required(views.FavoriteMixTapeList.as_view()), name='favorite_mixes'),
                       )
