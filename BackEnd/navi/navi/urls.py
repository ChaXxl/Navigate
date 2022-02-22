from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from django.urls import re_path

urlpatterns = [
    path('admin/', admin.site.urls),

    # 接口地址，包含api程序的urls
    path('api/', include('api.urls')),

    # 用于访问服务器本地图片。示例：https://map.chachal.xyz/static/imgs/11.jpg
    # 参考教程：http://t.csdn.cn/H8DOt
    re_path(r'^static/(?P<path>.*)', serve, {'document_root':'/home/xxl/Navigator/BackEnd/navi/static'})
]
