# coding: utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import pandas as pd
import json

from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.utils.safestring import SafeString

# Create your views here.
from django.contrib.auth.decorators import login_required
from .models import Task, Platform, PlatformConfig, GeneralConfig, PlatformKeys
from .models import Job, NewJob
from .forms import PlatformConfigForm, GeneralConfigForm, NewJobForm
from djproject.settings import DATABASES
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory, modelform_factory

from django.views.generic import RedirectView, TemplateView, ListView,DetailView, FormView, UpdateView
import re
import copy
import requests
from sqlalchemy import create_engine

engine = create_engine(
    'mysql+mysqldb://{}:{}@{}:3306/{}'.format(DATABASES['default']['USER'], DATABASES['default']['PASSWORD'],
                                              DATABASES['default']['HOST'],DATABASES['default']['NAME']),
    connect_args={'charset': 'utf8'},
    pool_size=8)

SERVER_URL = "http://101.200.184.162:6800"



class IndexView(TemplateView):
    template_name = 'videosearch/index.html'

class TastListView(ListView):
    template_name = 'videosearch/tasklist.html'
    model = Job

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

def brokermap(request):
    df = pd.read_excel('videosearch/data/zqgs.xlsx')
    grouped = df['name'].groupby(df['area'])
    se_counts = grouped.count()
    dict_counts = dict(se_counts)


    userData = []
    for ix, value in se_counts.iteritems():
        print ix, value
        zq_d = {'name': ix, 'value': value*100}
        userData.append(zq_d)

    encodejson = json.dumps(userData)
    # print repr(userData)
    # print encodejson
    return render(request, 'videosearch/broker-map.html', {'userData': SafeString(encodejson), 'dict_counts':dict_counts})

def listporjects(request):
    r = requests.get(SERVER_URL+'listprojects.json')
    encodejson = json.loads(r.text)
    projects = encodejson['projects']
    print projects

def jobs(request):

    # 获取可用的project
    url_p = SERVER_URL + "/listprojects.json"
    r = requests.get(url_p)
    enjson = json.loads(r.text)
    projects = enjson['projects']

    dfs = []


    for project in projects:
        url_j = SERVER_URL + "/listjobs.json?project={}".format(project)
        r = requests.get(url_j)
        enjson = json.loads(r.text)
        if enjson['status'] == 'ok':
            df_pending = pd.DataFrame(enjson['pending'])
            df_running = pd.DataFrame(enjson['running'])
            df_finished = pd.DataFrame(enjson['finished'])
            df_pending['status'] = 'pending'
            df_running['status'] = 'running'
            df_finished['status'] = 'finished'

            df = pd.concat([df_pending, df_running, df_finished])
            if len(df) == 0:
                continue
            df['node_name'] = enjson['node_name']
            df['project'] = project
            df['jobid'] = df['id']
            del df['id']
            print df.columns

            df['log'] = SERVER_URL + "/logs/" + project + "/" + df['spider'] + "/" + df['jobid'] + ".log"
            df['item'] = SERVER_URL + "/items/" + project + "/" + df['spider'] + "/" + df['jobid'] + ".jl"

            dfs.append(df)

    df_all = pd.concat(dfs, ignore_index=True)
    df_all[pd.isnull(df_all)] = '""'
    print df_all.head()

    sql = "delete from videosearch_job"
    engine.execute(sql)
    df.to_sql('videosearch_job', engine, index=False, if_exists='append')

    # pending_data = df_all[df_all['status']=='pending'].to_json(orient='records')
    # running_data = df_all[df_all['status'] == 'running'].to_json(orient='records')
    # finished_data = df_all[df_all['status'] == 'finished'].to_json(orient='records')
    #
    # datas = [pending_data, running_data, finished_data]
    # print running_data

    return HttpResponseRedirect("/videosearch/tasklist")
    # TastListView.as_view()


def addjob(request):

    url = SERVER_URL + "/listprojects.json"
    r = requests.get(url)
    enjson = json.loads(r.text)
    if enjson['status'] != 'ok':
        return HttpResponse("get projects list error!")

    projects = enjson['projects']
    spiders = []
    for project in projects:
        url = SERVER_URL + "/listspiders.json?project={}".format(project)
        r = requests.get(url)
        enjson_spiders = json.loads(r.text)
        if enjson_spiders['status'] == 'ok':
            for spider in enjson_spiders['spiders']:
                spiders.append(project+" : "+spider)

                # df = pd.DataFrame([(spider, project)], columns=['spider', 'project'])
                # df.to_sql('videosearch_newjob', engine, index=False, if_exists='append')

    # df_project = pd.DataFrame(projects, columns=['project'])
    # df_spider = pd.DataFrame(spiders, columns=['spider'])
    # df_project.to_sql('videosearch_project', engine, index=False, if_exists='append')
    # df_spider.to_sql('videosearch_spider', engine, index=False, if_exists='append')



    # newjob = NewJob.objects.last()
    # form = NewJobForm()#instance=newjob
    if request.method == 'POST':
        for key in request.POST:
            value = request.POST.get(key)
            print key, value
            project, spider = value.split(":")
            data = {"project":project.strip(),
                    "spider":spider.strip()}
            url = SERVER_URL + "/schedule.json"
            r = requests.post(url, data=data)
            return HttpResponse(r.text, status=200)

    return render_to_response('videosearch/newjob.html', {'spiders':spiders})

def canceljob(request, jobid):
    sql = "select * from videosearch_job where jobid='{}'".format(jobid)
    df = pd.read_sql(sql, engine)
    print df


    if request.method == 'POST':

        for key in request.POST:
            value = request.POST.get(key)
            print key, value


        if len(df):
            status = df.ix[0, 'status']
            result = ''
            if status in ('running', 'pending'):
                data = {'project': df.ix[0, 'project'],
                        'job': jobid}
                r = requests.post(SERVER_URL + '/cancel.json', data=data)
                result = r.text
            else:
                result = "jobid({}): 已经停止了, 本操作不起任何作用!".format(jobid)
        else:
            result = "找不到对应的jobid"
        return render_to_response('videosearch/success.html', {'data':result})


    return render_to_response('videosearch/canceljob.html', {'project': df.ix[0, 'project'],
                                                          'spider': df.ix[0, 'spider'],
                                                          'jobid': df.ix[0, 'jobid'],
                                                          'start_time': df.ix[0, 'start_time'],
                                                          'end_time': df.ix[0, 'end_time'],
                                                          'status': df.ix[0, 'status']})



# 111/160
# 193/200
# 90/120
# 79/120
# 90/120





