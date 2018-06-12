#!/usr/bin/env python3  
# -*- coding: utf-8 -*-  
"""  
 @desc:  
 @author: DYL  
 @contact: chng547835@163.com  
 @site: www.xxxx.com  
 @software: PyCharm  @since:python 3.5.2 on 2016/11/3.10:49  
 """
from django.conf.urls import url
from web.views import home

urlpatterns = [

    # (?P<name>)	给分组起个名字
    url(r'^all/(?P<article_type_id>\d+).html$', home.index,name='index'),


    url(r'^', home.index),
]
