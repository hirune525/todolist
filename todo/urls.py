# -*- coding:utf-8 -*-
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.todo_list, name='list'),
    url(r'^(?P<filter_mode>(all|done|process))/$',
        views.todo_list, name='list_filtered'),
    url(r'^add/$', views.todo_edit, name='add'),
    url(r'^edit/(?P<todo_id>\d+)/$', views.todo_edit,
        name='edit'),
    url(r'^checked/', views.todo_done, name='checked')
]
