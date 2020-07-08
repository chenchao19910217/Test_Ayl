from django.shortcuts import render

# Create your views here.
import hashlib,os

from django.http import HttpResponse
from django.shortcuts import render
import json

# Create your views here.
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import ensure_csrf_cookie
@csrf_exempt
@ensure_csrf_cookie
def index(request):

    return HttpResponse("index")