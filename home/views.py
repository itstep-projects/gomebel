from django.shortcuts import render
from news.models import Post


def index(request):
    data = dict()
    data['title'] = 'Главная'
    data['posts'] = Post.objects.order_by('-published')[:3]
    data['time'] = Post.objects.order_by('-published')[:3]
    return render(request, 'home/index.html', context=data)


def contacts(request):
    data = {'title': 'Контакты'}
    return render(request, 'home/contacts.html', context=data)


def about(request):
    data = {'title': 'О нас'}
    return render(request, 'home/about.html', context=data)
