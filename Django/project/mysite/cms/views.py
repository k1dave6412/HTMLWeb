from django.shortcuts import render , render_to_response
from django.http import HttpResponse
from .models import Restaurant,Food

def index (request):
    restaurant = Restaurant.objects.all()
    return render_to_response('cms/menu.html',locals())
