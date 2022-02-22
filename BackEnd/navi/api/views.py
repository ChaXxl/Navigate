from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.conf import settings

def img1(request):
    i = str(request.GET.get('i'))
    if i.isnumeric():
        path = f'/home/xxl/Navigator/BackEnd/navi/static/imgs/{i}.jpg'
    else:
        return ''
    with open(path, 'rb')as img:
        img = img.read()
    return HttpResponse(img, content_type='image/jpg')
   


def test(request):
    return JsonResponse({
        'status': 0,
        'name': '广州',
        'coordinates': {'lon': 113, 'lat': 23}
    })
