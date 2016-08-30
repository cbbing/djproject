# coding: utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from django.shortcuts import render, render_to_response
from django.views.generic import RedirectView, TemplateView, ListView,DetailView, FormView, UpdateView
from django.http import HttpResponse, HttpResponseRedirect
from bbcure.forms import CureDataForm
from bbcure.forms import CureDataImageForm
from models import CureData
from djproject.settings import MEDIA_ROOT

# Create your views here.
class IndexView(TemplateView):
    template_name = 'bbcure/index.html'

def handle_uploaded_file(f):
    with open(MEDIA_ROOT+'name.jpg', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def update_data(request):
    if request.method == 'POST':

        form = CureDataImageForm(request.POST or None, request.FILES or None)

        # form = CureDataForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save()
            print image.image.url
            # handle_uploaded_file(request.FILES['image'])

            cd = form.cleaned_data
            print cd
            # img_url = form['image']
            # print img_url
            # 根据用户提交的注册信息在用户信息表中建立一个新的用户对象
            # cureData = CureData.objects.create(
            #         name = form.cleaned_data['name'],
            #         cureDuration = form.cleaned_data['cureDuration'],
            #         create_at = form.cleaned_data['create_at'],
            #         note=form.cleaned_data['note'],
            #         image=form.cleaned_data['image'],
            #         operator=form.cleaned_data['operator'],
            #         status=form.cleaned_data['status'],
            #     )
            # cureData.save()
            return HttpResponseRedirect('/bbcure/success/')
    else:
        form = CureDataImageForm()
    return render_to_response('bbcure/data_form.html', {'form': form})



def success(request):
    return render_to_response('bbcure/success.html')

def search(request):
    if 'q' in request.GET:
        message = "You searched for:%r" % request.GET['q']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)