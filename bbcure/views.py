# coding: utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from django.shortcuts import render
from django.views.generic import RedirectView, TemplateView, ListView,DetailView, FormView, UpdateView

# Create your views here.
class IndexView(TemplateView):
    template_name = 'bbcure/index.html'