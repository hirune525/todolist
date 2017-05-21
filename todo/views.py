# -*- coding:utf-8 -*-
import json
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from todo.models import TodoItem
from todo.forms import TodoInputForm
from todo.utils import to_bool


@login_required
def todo_list(request, filter_mode='process'):
    ''' TODOの一覧 '''
    user = request.user
    if filter_mode == 'all':
        todos = TodoItem.objects.filter(create_user_id=user.id)
    elif filter_mode == 'done':
        todos = TodoItem.objects.filter(
            create_user_id=user.id,
            is_done=True)
    else:
        todos = TodoItem.objects.filter(
            create_user_id=user.id,
            is_done=False)
    todos = todos.order_by('limit_date', '-priority')
    return render(request, 'todo/list.html.j2', {
        'user': user, 'todos': todos, 'active_nav': filter_mode
    })


@login_required
def todo_edit(request, todo_id=None):
    ''' TODOの追加/編集 '''
    user = request.user
    if todo_id:
        todo_item = get_object_or_404(
            TodoItem,
            create_user_id=user.id,
            id=todo_id,
        )
        title = 'TODO参照/編集'
        active_nav = None
    else:
        todo_item = TodoItem()
        todo_item.create_user_id = user.id
        title = 'TODO追加'
        active_nav = 'add'

    if request.method == 'POST':
        form = TodoInputForm(request.POST, instance=todo_item)
        if form.is_valid():
            todo_item.save()
            return redirect('todo:list')
    else:
        form = TodoInputForm(instance=todo_item)

    return render(request, 'todo/edit.html.j2', {
        'user': user,
        'title': title,
        'form': form,
        'todo_id': todo_id,
        'active_nav': active_nav,
    })


@login_required
def todo_done(request, todo_id=None):
    user = request.user
    '''TODOの完了'''
    if request.method == 'POST':
        todo_id = request.POST['todo_id']
        is_done = request.POST['is_done']
        todo_item = TodoItem.objects.get(
            create_user_id=user.id,
            id=todo_id,
        )
        todo_item.is_done = to_bool(is_done)
        todo_item.save()
        response = json.dumps({})
        return HttpResponse(response, content_type="text/javascript")
    else:
        raise Http404
