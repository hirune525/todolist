# -*- coding:utf-8 -*-
from django.db import models
from accounts.models import TodoUser


class TodoItem(models.Model):
    CHOICE_PRIORITY = (
        (5, '★★★★★'), (4, '★★★★'), (3, '★★★'), (2, '★★'), (1, '★')
    )
    create_user = models.ForeignKey(
        TodoUser,
        verbose_name='作成者',
        related_name='TodoUser')
    task = models.CharField('タスク', max_length=256)
    contents = models.TextField('詳細', blank=True)
    priority = models.IntegerField('優先度', choices=CHOICE_PRIORITY)
    is_done = models.BooleanField('完了')
    limit_date = models.DateField('期限日', null=True)
    limit_time = models.TimeField('期限時間', null=True, blank=True)
    create_datetime = models.DateTimeField('作成日', auto_now=True)
    update_datetime = models.DateTimeField('更新日', auto_now_add=True)

    def __str__(self):
        return self.task
