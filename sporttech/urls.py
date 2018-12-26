from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf import settings
from django.urls import path, include

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from search import views as search_views
from home import views as home_views

urlpatterns = [
    url(r'^contact', home_views.contact, name='contact'),
    url(r'^accounts/', include('users.urls')),
    url(r'^showcase/', include('showcase.urls')),
    url(r'^api/', include('api.urls')),

    url(r'^player-stats', TemplateView.as_view(template_name='player_stats.html'), name='player_stats'),
    url(r'^club-stats', TemplateView.as_view(template_name='club_stats.html'), name='club_stats'),
    url(r'^media-info', TemplateView.as_view(template_name='media.html'), name='media'),
    url(r'^fan', TemplateView.as_view(template_name='fan.html'), name='fan'),
    url(r'^format', home_views.format, name='format'),

    # WAGTAIL
    url(r'^data-admin/', admin.site.urls),
    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),
    url(r'^search/$', search_views.search, name='search'),
    # needs to go last or will interfere with other urls. can't change to ^$ or will break for some reason
    url(r'', include(wagtail_urls)),
]

admin.site.site_header = 'SportTech IQ Admin Page'

# uncomment when you've figured out the static files issue
# if settings.DEBUG:
#     import debug_toolbar

#     urlpatterns += [
#         path('__debug__/', include(debug_toolbar.urls)),
#     ]