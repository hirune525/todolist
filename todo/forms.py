# -*- coding:utf-8 -*-
from django.forms import ModelForm
from todo.models import TodoItem


class TodoInputForm(ModelForm):
    '''TODOのフォーム'''

    def __init__(self, *args, **kwargs):
        super(TodoInputForm, self).__init__(*args, **kwargs)

        task_field = self.fields['task'].widget
        contents_field = self.fields['contents'].widget
        priority_field = self.fields['priority'].widget
        limit_date = self.fields['limit_date'].widget

        task_field.attrs['class'] = 'form-control'
        task_field.attrs['placeholder'] = 'タスク（必須）'

        contents_field.attrs['class'] = 'form-control'
        contents_field.attrs['placeholder'] = '詳細（任意）'

        priority_field.attrs['class'] = 'form-control'

        limit_date.input_type = 'date'
        limit_date.attrs['class'] = 'form-control'
        limit_date.attrs['placeholder'] = 'yyyy-mm-dd（任意）'

    class Meta:
        model = TodoItem
        fields = ('task', 'contents', 'priority', 'limit_date', 'is_done', )
