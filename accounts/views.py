from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import * 
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model, logout
# import django.contrib.auth
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import DataMixin

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm 
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:dashboard')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Logining")
        return dict(list(context.items()) + list(c_def.items())) 

    def form_valid(self, form):
        user = form.save()
        print(user)
        login(self.request, user)
        return redirect('accounts:dashboard')

    # def get_success_url(self):
    #     return reverse_lazy('dashboard')   


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'accounts/login.html'
    # success_url = reverse_lazy('accounts:dashboard')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Authorisation")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('accounts:dashboard')



def dashboard_view(request):
    # if request.user.is_authenticated:
    #     print('one')
    return render(request, 'accounts/dashboard.html', {'user': request.user})
    # else:
    #     print('two')
    #     return render(request, 'accounts/register.html')


def LogoutView(request):
    logout(request)
    return redirect('accounts:login')

def bbs(request):
    return render(request, "accounts/base.html")

