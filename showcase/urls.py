from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^scorecard/(?P<pk>\d+)/(?P<slug>[-\w\d\s]+)$', views.PlayerDetail, name="player_detail"),
    url(r'^generate-trading-card/(?P<pk>\d+)$', views.GenerateTradingCard, name="generate_trading_card")
]
