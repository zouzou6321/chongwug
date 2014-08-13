# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.utils import simplejson
def home_page_view(request):
    return render_to_response('index.html')