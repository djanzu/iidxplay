import os
from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LoginView, LogoutView
)
from django.views import generic
from .forms import LoginForm
from . import models
import pprint

# class Top(LoginRequiredMixin, generic.TemplateView):
#     template_name = '{app_name}/top.html'
#     login_url = '/login/'

#     def get(self, request):
#         self.template_name = self.template_name.format(app_name=request.resolver_match.app_name)
#         d = {
#             'full_name': request.user.full_name,
#             'username': request.user.username,
#         }
#         pprint.pprint(request.user)
#         print(request.user.full_name)
#         return render(request, self.template_name, d)


class Top(generic.TemplateView):
    template_name = 'myfavs/top.html'



class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'myfavs/login.html'

    # def post(self, request):
    #     print(request)


class Logout(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name = 'myfavs/logout.html'

    def get(self, request):
        self.template_name = self.template_name.format(app_name=request.resolver_match.app_name)
        return render(request, self.template_name)

