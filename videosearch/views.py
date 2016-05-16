# coding: utf-8

from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponseRedirect

# Create your views here.
from django.contrib.auth.decorators import login_required
from .models import Task, Platform, PlatformConfig, GeneralConfig, PlatformKeys
from .forms import PlatformConfigForm, GeneralConfigForm

from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory, modelform_factory

from django.views.generic import RedirectView, TemplateView, ListView,DetailView, FormView, UpdateView
import re
import copy

class IndexView(TemplateView):
    template_name = 'videosearch/index.html'

class TastListView(ListView):
    template_name = 'videosearch/tasklist.html'
    model = Task

# class TaskDetailView(DetailView):
#     template_name = 'videosearch/taskdetail.html'
#     model = Task
#
#
#     def get_context_data(self, **kwargs):
#         context = super(TaskDetailView, self).get_context_data(**kwargs)
#         #context['now'] = timezone.now()
#         return context


@login_required(login_url='/login/')
def general_config(request):

    config = GeneralConfig.objects.last()
    form = GeneralConfigForm(instance=config)
    if request.method == 'POST':
        for key in request.POST:
            value = request.POST.getlist(key)
            print key, value
        form = GeneralConfigForm(request.POST)
        if form.is_valid():
            # GeneralConfig.objects.all().delete() #清空
            form.save()
        return HttpResponseRedirect('/')
    return render_to_response('videosearch/generalconfig.html', locals())

@login_required(login_url='/login/')
def platform_config(request):

    platformConfigFormSet = modelformset_factory(PlatformConfig,
                                                 fields="__all__",
                                                 extra=0)

    if request.method == 'POST':
        for key in request.POST:
            value = request.POST.getlist(key)
            print key, value

        print len(PlatformConfig.objects.all())
        platformconfigs = [copy.deepcopy(cf) for cf in PlatformConfig.objects.all()]
        PlatformConfig.objects.all().delete() # 清空

        for config in platformconfigs:
            print config.platform.id
            pc = PlatformConfig()
            for key in request.POST:
                value = request.POST.getlist(key)
                value = True if value == [u'on'] else False

                f = re.search('-(\d+)-(.*)', key)
                if not f:
                    break
                id = int(f.group(1))+1
                p_key = f.group(2)
                if id == config.platform.id:
                    if p_key == u'platform':
                        pc.platform = Platform.objects.get(pk=id)
                    elif p_key == u'lentype_all':
                        pc.lentype_all = value
                    elif p_key == u'lentype_0_10':
                        pc.lentype_0_10 = value
                    elif p_key == u'lentype_10_30':
                        pc.lentype_10_30 = value
                    elif p_key == u'lentype_30_60':
                        pc.lentype_30_60 = value
                    elif p_key == u'lentype_60_More':
                        pc.lentype_60_More = value

            print pc
            pc.save()
        return HttpResponseRedirect('/')
        # return HttpResponseRedirect('/videosearch/platformconfig')

    return render_to_response('videosearch/platformconfig.html', locals())



def index(request):
    lastest_task_list = Task.objects.order_by('-create_at')
    context = { 'lastest_task_list':lastest_task_list}
    return render(request, 'videosearch/index.html', context)

def task_detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    platformconfigs = PlatformConfig.objects.all()

    class Tab():
        def __init__(self, id, platform):
            self.id = id
            self.platform = platform

    tabPlatforms = []
    for i in range(len(platformconfigs)):
        tab = Tab(i+1, platformconfigs[i])
        tabPlatforms.append(tab)

    tabPlatforms_active = tabPlatforms[0]
    tabPlatforms_others = tabPlatforms[1:]

    return render(request, 'videosearch/taskdetail.html', locals())

def keys_list(request):
    objects = PlatformKeys.objects.all()

    print objects

def platforms(request):
    platforms = Platform.objects.all()

    return render_to_response('videosearch/platforms.html', locals())
    #return render(request, 'videosearch/platforms', {'platforms':Task.objects})




