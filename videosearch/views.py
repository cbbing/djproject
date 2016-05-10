from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponseRedirect

# Create your views here.
from django.contrib.auth.decorators import login_required
from .models import Task, Platform, PlatformConfig, GeneralConfig
from .forms import PlatformConfigForm

from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory

from django.views.generic import RedirectView, TemplateView, ListView, FormView, UpdateView


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

class IndexView(TemplateView):
    template_name = 'videosearch/index.html'



    # def get_context_data(self, **kwargs):
    #     context = super(IndexView, self).get_context_data(**kwargs)
    #     userobj = Platform.objects.filter(site='youku')
    #     if userobj:
    #         context['loginname'] = userobj[0].name
    #         context = dict(context, **userobj)
    #     #else:
    #     return context


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

def platform_config(request):
    platformconfigs = PlatformConfig.objects.all()
    # for config in platformconfigs:
    #     platform = config.platform.name

    generalConfigFormSet = modelformset_factory(GeneralConfig, fields=('page_count', 'key_from'), extra=0)

    platformConfigFormSet = modelformset_factory(PlatformConfig,
                                                 fields=('platform', 'lentype_all',
                                                         'lentype_0_10','lentype_10_30',
                                                         'lentype_30_60','lentype_60_More'),
                                                 extra=0)

    if request.method == 'POST':
        formset = platformconfigs(request.POST)
        formset.save()
        return #render_to_response('platformconfig.html', locals())
    # else:
    #     formset = platformconfigs()


    return render_to_response('videosearch/platformconfig.html', locals())