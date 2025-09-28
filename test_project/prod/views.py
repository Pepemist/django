from django.shortcuts import render

def index(request):
    context = {
        'title': 'Test Title',
        'is_promotion': False,
    }
    return render(request, 'index.html', context)

def products(request):
    context = {
        'title': 'Products page',
        'products': [
            {
                'img': '/static/img/1.png',
                'name': 'first prod',
                'price': 6060,
                'desc': 'Первая картинка для теста'
            },
            {
                'img': '/static/img/2.png',
                'name': '2nd prod',
                'price': 5000,
                'desc': 'Вторая картинка для теста'
            },
            {
                'img': '/static/img/3.png',
                'name': '3rd prod',
                'price': 6000,
                'desc': 'Третья картинка для теста'
            },
        ]
    }
    return render(request, 'prod.html', context)