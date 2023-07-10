from django.shortcuts import render

# Create your views here.

from app.models import *

from django.http import HttpResponse

def Insert_topic(request):
    tn=input('Enter The Topic')
    To=Topic.objects.get_or_create(topic_name=tn)[0]
    To.save()
    return HttpResponse ('Create Topic')

def Insert_web(request):
    tn=input('Enter The Topic')
    To=Topic.objects.get_or_create(topic_name=tn)[0]
    To.save()
    Wn=input('Enter The Name')
    Wu=input('Enter The url')
    Wo=Webpage.objects.get_or_create(topic_name=To,name=Wn,url=Wu)[0]
    return HttpResponse ('Create Webpage')



