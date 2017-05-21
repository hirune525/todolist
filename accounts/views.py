# -*- coding:utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def user_profile(request):
    context = {'user': request.user}
    return render(request, 'accounts/profile.html.j2', context)
