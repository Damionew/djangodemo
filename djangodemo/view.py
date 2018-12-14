"""
视图对象
"""
from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    # 相当于Spring中RequestMapping、ResponseBody返回json字符串
    return HttpResponse("Hello world ! ")

def index(request):
    # 相当于Spring中RequestMapping返回页面
    return render(request, 'index.html')