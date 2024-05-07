from django.shortcuts import render
from django.http import HttpResponse
import datetime

from relecloud.models import Destination
# Create your views here.
def index(request):
    return render(request,'relecloud/index.html')

def about(request):
    date = datetime.datetime.now()
    return render(request,'relecloud/about.html',{'date':date})


def destination(request):
    all_destination = Destination.objects.all()
    return render(request,'relecloud/destination.html',{'destinations':all_destination})