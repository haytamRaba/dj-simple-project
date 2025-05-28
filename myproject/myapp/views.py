from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

def index(response):
  return HttpResponse("<h2>hey!<h2>")
def index2(respose):
  return HttpResponse("second page !!!!!!!!!!!")
def index3(response):
  return HttpResponse("index2/index3")