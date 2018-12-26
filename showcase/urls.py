from django.conf.urls import url

from . import views

# app_name = 'showcase'

urlpatterns = [
	url(r'^$', views.ScorecardListView.as_view(), name='index'), # not used
	url(r'^(?P<pk>\d+)$', views.ShowcaseDetail, name="showcase_detail"), # not used
	url(r'^scorecard/(?P<pk>\d+)/(?P<slug>[-\w\d]+)$', views.PlayerDetail, name="player_detail"),
	url(r'^generate-trading-card/(?P<pk>\d+)/(?P<first>[-\w\d]+)/(?P<last>[-\w\d]+)$', views.GenerateTradingCard, name="generate_trading_card"),
	#url(r'^team/(?P<pk>\d+)$', views.PlayerScorecardDetailView.as_view(), name="TeamDetail"), # not used yet
	]
	