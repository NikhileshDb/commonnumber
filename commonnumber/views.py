from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.forms import ModelForm
from . models import *
from datetime import date
from .forms import *
from .filters import NumberFilter
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . serializers import TeerResultSerializer



def home(request):
    resultNum = TeerResult.objects.all().order_by('-date',)
    myFilter = NumberFilter(request.GET, queryset=resultNum)
    resultNum = myFilter.qs
    context = {
        'myFilter': myFilter,
        'resultNum': resultNum,
  
    }
    return render(request, 'commonnumber/index.html', context)

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Result List': '/result-list/',
        'Result Detail': '/result-detail/<str=date>',   
    }
    return Response(api_urls)


@api_view(['GET'])
def ResultList(request):
    results = TeerResult.objects.all()
    serializer = TeerResultSerializer(results, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ResultDetail(request,pk):
    results = TeerResult.objects.get(date=pk)
    serializer = TeerResultSerializer(results, many=False)
    return Response(serializer.data)








