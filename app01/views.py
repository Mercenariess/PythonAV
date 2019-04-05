from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.


def login(request):
    """
    登陆
    :param request:
    :return:
    """
    return render(request, "bam_login.html")

def index(request):
    """
    主页
    :param request:
    :return:
    """
    return render(request,"index.html")


def bam(request):
    """
    后台管理
    :param request:
    :return:
    """
    return render(request, 'bam_index.html')

def  article(request):
    return