from django.conf.urls.defaults import *
from models import Node

import views
urlpatterns = patterns('',
    (r'^$',  'django.views.generic.simple.direct_to_template', {'template': 'req/index.html',
                                                                'extra_context':{
                                                                    'nodes':Node.objects.filter(parent__isnull=True).order_by('index')
                                                                } }), 
    (r'^node/(?P<id>.*)/$', views.node),
    (r'^node/(?P<id>.*)/admin/$', views.admin),
    (r'^node/(?P<node_id>.*)/item/(?P<id>.*)/$', views.item),
)
