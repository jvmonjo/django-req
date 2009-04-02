#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from models import *

def node(request, id, template='req/node.html'):
    dict = {'node':Node.objects.get(pk=int(id))}
    return render_to_response(template,dict, context_instance=RequestContext(request))
