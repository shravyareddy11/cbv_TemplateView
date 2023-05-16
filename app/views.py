from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import TemplateView
from app.forms import *
from django.http import HttpResponse
# Create your views here.
class cbv_context(TemplateView):
    template_name='cbv_context.html'

    def get_context_data(self, **kwargs) :
        EDCO=super().get_context_data(**kwargs)
        
        EDCO['name']="shravya"
        EDCO['age']=21
        return EDCO
class cbv_form(TemplateView):
    template_name='cbv_form.html'

    def get_context_data(self, **kwargs): 
        EDCO=super().get_context_data(**kwargs)
        SO=Studentform()
        EDCO['SO']=SO
        return EDCO
    def post(self,request):
        SOF=Studentform(request.POST)
        if SOF.is_valid():
            SOF.save()
        return HttpResponse('insertion successfully')






