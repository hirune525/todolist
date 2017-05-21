# -*- coding:utf-8 -*-
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    url(r'^profile/$', views.user_profile, name='user_profile'),
    url(r'^login/$', auth_views.login,
        {'template_name': 'accounts/login.html.j2'}, name='login'),
    url(r'^logout/$', auth_views.logout,
        {'template_name': 'accounts/logged_out.html.j2'}, name='logout'),
]
