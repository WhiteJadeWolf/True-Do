from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("You are at TrueDo homepage.")
    return render(request,'home/index.html')