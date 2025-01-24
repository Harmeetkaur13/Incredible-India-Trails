from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def destination(request):
	return HttpResponse("Hello!")

