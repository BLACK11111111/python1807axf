from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    title='首页'
    return render(request,'home/home.html',context={'title':title})


