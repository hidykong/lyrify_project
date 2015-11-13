# lyrify urls
from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns(
    'lyrify.views',
    url(r'^$', 'home'),
    url(r'^create_post/$', 'create_post'),
    url(r'^check_answer/$', 'check_answer'),
    url(r'^(?P<post_id>[0-9]+)/$', views.test , name='test'),
    
)
