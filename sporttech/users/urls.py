from django.conf.urls import url
from django.contrib.auth import views as auth_views

from users import views

urlpatterns = [
	url(r'^profile', views.AccountProfile, name="account_profile"),
	url(r'^coach-profile', views.CoachProfile, name="coach_profile"),
	url(r'^player-profile', views.PlayerProfile, name="player_profile"),
    url(r'^registration$', views.Registration, name='player_registration'),
    url(r'^signup', views.Signup, name='signup'),
    url(r'^login', auth_views.login, name='login'),
    url(r'^logout', auth_views.logout, name='logout'),
    url(r'^password-reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password-reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
	]
