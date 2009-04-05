#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from models import *

def node(request, id, view_id=None, template='req/node%s.html'):
    node = Node.objects.get(pk=int(id))
    if view_id:
        view = View.objects.get(node=node, pk=int(view_id))
    else:
        view = View.objects.get(node=node, title='Standard')
    template_gen = template % ""
    template = template % ("-" + node.type)
    node.display_view(view)
    dict = {'node':node, 'view':view}
    return render_to_response((template, template_gen),dict, context_instance=RequestContext(request))

def admin(request):
    return None

def item(request):
    return None