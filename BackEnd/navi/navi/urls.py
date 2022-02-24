from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from tile import views


urlpatterns = [
    path('admin/', admin.site.urls),

    # 接口地址，包含api程序的urls
    path('api/', include('api.urls')),

    # 获取切片的接口,调用tile/views.py里的img方法
    path('tile/', views.img),

    # 用于访问服务器本地图片。示例：https://map.chachal.xyz/static/imgs/11.png
    # 参考教程：http://t.csdn.cn/H8DOt
    re_path(r'^static/(?P<path>.*)', serve, {'document_root':'/home/xxl/Navigator/BackEnd/navi/static'})
]
