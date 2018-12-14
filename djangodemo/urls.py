"""
绑定URL与视图函数
"""
from django.conf.urls import url
from djangodemo.view import index


urlpatterns = [
    url(r'^index/', index)
]