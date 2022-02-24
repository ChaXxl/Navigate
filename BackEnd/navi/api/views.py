from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.conf import settings


def img(request):
    """根据图片的x、y、z返回对应切片"""
    x = str(request.GET.get('x'))
    y = str(request.GET.get('y'))
    z = str(request.GET.get('z'))

    # xyz全部都为数字
    flag = all([
        x.isnumeric(),
        y.isnumeric(),
        z.isnumeric()
    ])
    if flag:
        path = f'{settings.STATICFILES_DIRS[0]}/{z}.png'
    else:
        return ''
    return HttpResponse(getImg(path), content_type='image/png')
    

def getImg(img_path):
    """打开图片返回"""
    with open(img_path, 'rb')as f:
        img = f.read()
    return img


