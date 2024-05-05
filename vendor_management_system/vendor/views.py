from django.shortcuts import render
from django.views import View
from django.http.request import HttpRequest
from django.http.response import JsonResponse


# Create your views here.
class Vendor(View):
    def post(self,request:HttpRequest):
        return JsonResponse({'message':'vendor api called'},status=200)

    def get():
        pass

class OnVEndor(View):
    def get():
        pass

    def patch():
        pass

    def delete():
        pass
    
