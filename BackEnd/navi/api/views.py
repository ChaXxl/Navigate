from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def test(request):
    # return HttpResponse('这是个测试页面...')
    return JsonResponse({
        'status': 200,
        'name': '广州',
        'data': [113, 23]
    })
