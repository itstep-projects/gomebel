from django.shortcuts import render, redirect
from .forms import ProjectForm
from .models import Project, Category
from django.contrib.auth import logout
from django.core.paginator import Paginator


def index(request):
    data = dict()
    data['title'] = 'Проекты'
    all_projects = Project.objects.all()
    data['projects'] = all_projects

    paginator = Paginator(all_projects, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data['page_obj'] = page_obj
    return render(request, 'projects/index.html', context=data)


def details(request, project_id):
    data = dict()
    data['title'] = 'Проект детальнее'
    data['pre_href'] = 'projects'
    data['pre_title'] = 'Проекты'
    data['project'] = Project.objects.get(id=project_id)
    return render(request, 'projects/details.html', context=data)


def create(request):
    data = dict()
    data['title'] = 'Добавление Проекта'
    data['pre_href'] = 'projects'
    data['pre_title'] = 'Проекты'
    if request.method == 'GET':
        # Блокировка доступа через адресную строку!)))
        if request.user.username == 'superadmin':
            data['form'] = ProjectForm()
            return render(request, 'projects/create.html', context=data)
        else:
            logout(request)
            return redirect('/accounts/sign_up')
        # ============================================
    elif request.method == 'POST':
        filled_form = ProjectForm(request.POST, request.FILES)
        filled_form.save()
        return redirect('/projects')


def edit(request):
    data = dict()
    data['title'] = 'Редактирование'
    data['pre_href'] = 'projects'
    data['pre_title'] = 'Проекты'
    return render(request, 'projects/edit.html', context=data)


def delete(request):
    data = dict()
    data['title'] = 'Удаление'
    data['pre_href'] = 'projects'
    data['pre_title'] = 'Проекты'
    return render(request, 'projects/delete.html', context=data)
