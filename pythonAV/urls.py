"""pythonAV URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,include
from app01.views import index
from app01.views import bam
from app01.views import login


urlpatterns = [
    path('admin/', admin.site.urls),
    # 主业
    re_path('^index/$', index),
    # 后台管理主页
    re_path("^bam/$", bam),
    # 后台管理 增删改查
    re_path("^bam/", include("bam.url")),
    # 后台管理 登陆
    re_path("^bam/login/$",login)
]
