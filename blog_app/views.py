from django.shortcuts import render
from django.views import View
from blog_app.models import Blog
# Create your views here.

class base(View):
    def get(self,request,*args, **kwargs):
        return render(request,'base.html')

class lists(View):
    def get(self,request,*args, **kwargs):
        blogs=Blog.objects.all()
        return render(request,'lists.html',{'blogs':blogs})

class detail(View):
    def get(self,request,slug,*args, **kwargs):
        blog=Blog.objects.get(slug=slug)
        return render(request,'detail.html',{'blog':blog})