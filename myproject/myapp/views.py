from django.shortcuts import render
from django.http import HttpResponse 
from .models import ToDoList , Item
from .forms import CreateNewList
# Create your views here.

def index(response,id):
  ls = ToDoList.objects.get(id=id)
 
  return render(response,"base/list.html",{"ls":ls} )

def create(response):
  form = CreateNewList()
  return render(response,"base/create.html",{"form":form})

def home(response):
  return render(response,"base/home.html",{})