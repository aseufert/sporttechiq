from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from api import views

# app_name = 'api'

urlpatterns = [
    url(r'^players$', views.PlayerList.as_view()),
    url(r'^players/(?P<pk>[0-9]+)$', views.PlayerDetail.as_view()),
    url(r'^users$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)$', views.UserDetail.as_view()),
    url(r'^users/profile$', views.UserProfile.as_view()),
    url(r'^clubs$', views.ClubList.as_view()),
    url(r'^clubs/(?P<pk>[0-9]+)$', views.ClubDetail.as_view()),
    url(r'^teams$', views.TeamList.as_view()),
    url(r'^teams/(?P<pk>[0-9]+)$', views.TeamDetail.as_view()),
    url(r'^showcase$', views.ShowcaseList.as_view()),
    url(r'^showcase/(?P<pk>[0-9]+)$', views.ShowcaseDetail.as_view()),
    url(r'^coaches$', views.CoachList.as_view()),
    url(r'^coaches/(?P<pk>[0-9]+)$', views.CoachDetail.as_view()),
    url(r'^directors/(?P<pk>[0-9]+)$', views.DirectorDetail.as_view()),
    url(r'^scorecard$', views.PlayerScorecardList.as_view()),
    url(r'^stations$', views.StationList.as_view()),
    url(r'^field-layouts$', views.FieldLayoutList.as_view()),
    # auth token urls
    url(r'^login-token$', obtain_jwt_token),
    url(r'^api-token-refresh$', refresh_jwt_token),
    url(r'^api-token-verify$', verify_jwt_token),
]