from django.shortcuts import render
from django.template.loader import get_template
from django.template import RequestContext
from django.template.context import Context
from django.http import HttpResponse
import json

def home(request):
    return render(request, 'index.html')