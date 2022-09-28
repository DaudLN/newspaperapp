from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class HomePageView(TemplateView):
    template_name = 'home.html'


# class PasswordChange(TemplateView):
#     template_name = 'password_change_form.html'
