# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response

from django.http import HttpResponse


def sample_index(request):
    return render(request, 'website/index.html', {})

# # Create your views here.
# def sample_index(request):
#     return render_to_response('index.html')