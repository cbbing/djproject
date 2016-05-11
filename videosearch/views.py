# coding: utf-8

from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponseRedirect

# Create your views here.
from django.contrib.auth.decorators import login_required
from .models import Task, Platform, PlatformConfig, GeneralConfig
from .forms import PlatformConfigForm, GeneralConfigForm

from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory, modelform_factory

from django.views.generic import RedirectView, TemplateView, ListView, FormView, UpdateView
import re

class IndexView(TemplateView):
    template_name = 'videosearch/index.html'

class TaskList(ListView):
    template_name = 'videosearch/index.html'

    model = Task

# class PlatformConfig(FormView):
#
#     template_name = 'videosearch/platformconfig.html'
#
#     form_class = PlatformConfig
#
#     generalConfigFormSet = modelformset_factory(GeneralConfig, fields=('page_count', 'key_from'), extra=0)
#
#     platformConfigFormSet = modelformset_factory(PlatformConfig,
#                                                  fields=('platform', 'lentype_all',
#                                                          'lentype_0_10', 'lentype_10_30',
#                                                          'lentype_30_60', 'lentype_60_More'),
#                                                  extra=0)





    # def get_context_data(self, **kwargs):
    #     context = super(IndexView, self).get_context_data(**kwargs)
    #     userobj = Platform.objects.filter(site='youku')
    #     if userobj:
    #         context['loginname'] = userobj[0].name
    #         context = dict(context, **userobj)
    #     #else:
    #     return context

class GeneralConfigView(FormView):
    template_name = 'videosearch/generalconfig.html'

    model = GeneralConfig

    form_class = GeneralConfigForm
    success_url = '/videosearch/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super(GeneralConfigForm, self).form_valid(form)


@login_required(login_url='/login/')
def index(request):
    lastest_task_list = Task.objects.order_by('-create_at')
    context = { 'lastest_task_list':lastest_task_list}
    return render(request, 'videosearch/index.html', context)

def detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'videosearch/detail.html', {'task':task})

def platforms(request):
    platforms = Platform.objects.all()

    return render_to_response('videosearch/platforms.html', locals())
    #return render(request, 'videosearch/platforms', {'platforms':Task.objects})

def general_config(request):

    config = GeneralConfig.objects.last()
    form = GeneralConfigForm(instance=config)
    if request.method == 'POST':
        for key in request.POST:
            value = request.POST.getlist(key)
            print key, value
        form = GeneralConfigForm(request.POST)
        if form.is_valid():
            #GeneralConfig.objects.all().delete() #清空
            form.save()
        return HttpResponseRedirect('/')
    return render_to_response('videosearch/generalconfig.html', locals())


def platform_config(request):
    platformconfigs = PlatformConfig.objects.all()
    # for config in PlatformConfig.objects.all():


    platformConfigFormSet = modelformset_factory(PlatformConfig,
                                                 fields="__all__",
                                                 extra=0)

    if request.method == 'POST':
        for key in request.POST:
            value = request.POST.getlist(key)
            print key, value

        print len(PlatformConfig.objects.all())

        for config in PlatformConfig.objects.all():
            print config.platform.id
            pc = PlatformConfig()
            # for key in request.POST:
            #     value = request.POST.getlist(key)
            #     value = True if value == [u'on'] else False
            #
            #     f = re.search('-(\d+)-(.*)', key)
            #     if not f:
            #         break
            #     id = int(f.group(1))+1
            #     p_key = f.group(2)
            #     if id == config.platform.id:
            #         if p_key == u'platform':
            #             pc.platform = Platform.objects.get(pk=id)
            #         elif p_key == u'lentype_all':
            #             pc.lentype_all = value
            #         elif p_key == u'lentype_0_10':
            #             pc.lentype_all = value
            #         elif p_key == u'lentype_10_30':
            #             pc.lentype_all = value
            #         elif p_key == u'lentype_30_60':
            #             pc.lentype_all = value
            #         elif p_key == u'lentype_60_More':
            #             pc.lentype_all = value
            #
            # print pc
            # pc.save()


        # formset = platformconfigs(request.POST)
        # formset.save()
        return HttpResponseRedirect('/')



    return render_to_response('videosearch/platformconfig.html', locals())