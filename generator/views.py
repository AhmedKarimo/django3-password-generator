from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request,'generator/home.html',{'password':'fasjfakjfia5'})

def about(request):
    return render(request, 'generator/about.html')


def password(request):


    chars = list('abcdefghijklmonpqrstuvwxyz')

    if request.GET.get('uppercase'):
        chars.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYW'))
    if request.GET.get('special'):
        chars.extend(list('~!@#$%^&&*'))
    if request.GET.get('numbers'):
        chars.extend(list('0123456789'))


    length = int(request.GET.get('length',12))

    thepass = ''

    for x in range(length):
        thepass += random.choice(chars)




    return render(request,'generator/passowrd.html',{'pass':thepass})
