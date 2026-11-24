from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
def hello_world(request):
    return HttpResponse("Hello World!")

# inherit from view
class hello_philippines(View):
    def get(self, request):
        return HttpResponse("UYYYY PILIPINES!!!!")