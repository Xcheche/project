from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def index(request):
    return render(request,'relecloud/index.html')

def about(request):
    date = datetime.datetime.now()
    return render(request,'relecloud/about.html',{'date':date})