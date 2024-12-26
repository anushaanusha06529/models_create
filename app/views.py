from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.

def insert_topic(request):
    tn=input('enter topicname')
    TOD=Topic.objects.get_or_create(topic_name=tn)
    if TOD[1]:
        return HttpResponse('new topic is created')
    else:
        return HttpResponse('given topic is already present')
    

def insert_webpage(request):
    tn=input('enter a topic name')
    name=input('enter a name')
    url=input('enter url')
    LTO=Topic.objects.filter(topic_name=tn)
    if LTO:
        WTOD=Webpage.objects.get_or_create(topic_name=LTO[0],name='a',url=url)
        if WTOD[1]:
            return HttpResponse('web page is created')
        else:
            return HttpResponse('web page is already present')
    else:
        return HttpResponse('give topic is not present in given parent table object')    

def insert_accessrecords(request):
    pk=int(input('enter webpage pk'))
    name = input("Enter the webpage name: ")
    author = input("Enter the author name: ")
    date = input("Enter the date (YYYY-MM-DD): ")
    
   
    wq= Webpage.objects.filter(pk=pk)
    if wq:
       
       
        AR_TOD = AccessRecords.objects.get_or_create(webpage=wq, author=author, date=date)
        if AR_TOD[1]:
            return HttpResponse("AccessRecord is created")
        else:
            return HttpResponse("AccessRecord is already present")
    else:
        return HttpResponse("The specified webpage does not exist in the Webpage table")
