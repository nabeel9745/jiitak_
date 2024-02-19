from urllib import request
from django.shortcuts import render,redirect
from django.http import HttpResponse


# Create your views here.


# def first_app(request):
#         return render(request,'samples.html') 
def print_hello(request):
    personal_details={
        'name':'Nabeel',
        'native_language':'Malayalam',
        'Hobbies':'travelling,football'
    }
    return render(request,'samples.html',personal_details)
 

