from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm, PostForm2
from django.contrib.auth import logout
from django.core.paginator import Paginator


def index(request):
    data = dict()
    data['title'] = 'Лента новостей'
    all_posts = Post.objects.order_by('-published')
    data['posts'] = all_posts

    paginator = Paginator(all_posts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data['page_obj'] = page_obj

    return render(request, 'news/index.html', context=data)


def create(request):
    data = dict()
    data['title'] = 'Добавление новости'
    data['pre_href'] = 'news'
    data['pre_title'] = 'Новости'
    if request.method == 'GET':
        # Блокировка доступа через адресную строку!)))
        if request.user.username == 'superadmin':
            data['form'] = PostForm()
            return render(request, 'news/create.html', context=data)
        else:
            logout(request)
            return redirect('/accounts/sign_up')
        # ============================================
    elif request.method == 'POST':
        filled_form = PostForm(request.POST, request.FILES)
        filled_form.save()
        return redirect('/news')


def details(request, post_id):
    data = dict()
    data['title'] = 'Просмотр новости'
    data['post'] = Post.objects.get(id=post_id)
    data['pre_href'] = 'news'
    data['pre_title'] = 'Новости'
    return render(request, 'news/details.html', context=data)


def edit(request, post_id):
    data = dict()
    data['title'] = 'Редактирование новости'
    data['pre_href'] = 'news'
    data['pre_title'] = 'Новости'
    post = Post.objects.get(id=post_id)
    if request.method == 'GET':

        # Блокировка доступа через адресную строку!)))
        if request.user.username == 'superadmin':
            data['form'] = PostForm2(instance=post)
            data['post'] = post
            return render(request, 'news/edit.html', context=data)
        else:
            logout(request)
            return redirect('/accounts/sign_up')
        # ============================================

    elif request.method == 'POST':
        form2 = PostForm2(request.POST)
        if form2.is_valid():
            post.title = form2.cleaned_data['title']
            post.about = form2.cleaned_data['about']
            post.text = form2.cleaned_data['text']
            post.author = form2.cleaned_data['author']
            post.save()
        return redirect('/news')


def delete(request, post_id):
    data = dict()
    data['title'] = 'Удаление новости'
    data['pre_href'] = 'news'
    data['pre_title'] = 'Новости'
    post = Post.objects.get(id=post_id)
    if request.method == 'GET':

        # Блокировка доступа через адресную строку!)))
        if request.user.username == 'superadmin':
            data['post'] = post
            return render(request, 'news/delete.html', context=data)
        else:
            logout(request)
            return redirect('/accounts/sign_up')
        # ============================================

    elif request.method == 'POST':
        post.delete()
        return redirect('/news')
