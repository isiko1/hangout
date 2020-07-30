# from https://studygyaan.com/django/how-to-add-social-login-to-django

from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "home.html"
