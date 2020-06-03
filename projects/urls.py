from django.urls import path, re_path
from .views import index, details, create, edit, delete

urlpatterns = [
    path('', index),
    path('index', index),
    path('create', create),
    re_path(r'^details/(?P<project_id>[0-9]+)$', details),
    re_path(r'^edit/(?P<project_id>[0-9]+)$', edit),
    re_path(r'^delete/(?P<project_id>[0-9]+)$', delete)
]