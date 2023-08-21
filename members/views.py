from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

# def members(request):
#     return HttpResponse("Hello world!")

 
# def oranos(request):
#     return HttpResponse("Hello,this is oranos!")
   
# def azim(request):
#     return HttpResponse("Hello,this is azim!")



def members(request):
  mymembers = Member.objects.all().values()

  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context,request))



