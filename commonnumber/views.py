from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import ModelForm
from . models import *
from datetime import date
from .forms import *
from .filters import NumberFilter



        

def firstDigit(x):
    # Remove last digit from number
    # till only one digit is left
    while x >= 10:
        x = x / 10;
        return int(x)





def home(request):
    #resultdate = Result.objects.all()
    resultNum = TeerResult.objects.all().order_by('-date',)
    myFilter = NumberFilter(request.GET, queryset=resultNum)
    resultNum = myFilter.qs


    context = {
        'myFilter': myFilter,
        'resultNum': resultNum,
  
    }
    return render(request, 'commonnumber/index.html', context)













