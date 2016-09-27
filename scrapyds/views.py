#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
import requests
import json
import pandas as pd

site = "http://101.200.184.162:6800"

def jobs(request):

    # 获取可用的project
    url_p = site + "/listprojects.json"
    r = requests.get(url_p)
    enjson = json.loads(r.text)
    projects = enjson['projects']

    dfs = []


    for project in projects:
        url_j = site + "/listjobs.json?project={}".format(project)
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
            df['node_name'] = enjson['node_name']
            dfs.append(df)

    df_all = pd.concat(dfs, ignore_index=True)
    print df_all.head()

    json_data = df_all.to_json(orient='records')
    json_data = json_data.replace('null', '""')
    # print
    return HttpResponse(json_data)
    # return HttpResponseRedirect(site + '/jobs')

def listprojects(requests):
    url = site + '/jobs'
    r = requests.get(url)
    enjson = json.loads(r.text)
    return HttpResponse(r.text)

