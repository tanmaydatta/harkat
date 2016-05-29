from django.shortcuts import render
import requests
from django.template import Context
from django.http import *
from django.template.loader import get_template
from django.views.decorators.csrf import *
# from auth import *
from .models import *
import json

# Create your views here.
def hello(request):
	return HttpResponse("Hello, world.")