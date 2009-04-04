#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from models import *

def node(request, id, template='req/node%s.html'):
    node = Node.objects.get(pk=int(id))
    template_gen = template % ""
    template = template % ("-" + node.type)
    dict = {'node':node}
    return render_to_response((template, template_gen),dict, context_instance=RequestContext(request))

def admin(request):
    return None

def item(request):
    return None