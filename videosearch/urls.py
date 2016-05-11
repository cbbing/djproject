from django.conf.urls import url

from . import views

urlpatterns = [

    # ex : /videosearch/
    url(r'^$', views.IndexView.as_view()),
    url(r'^platformconfig$', views.platform_config, name='platformconfig'),
    url(r'^generalconfig$', views.general_config, name='generalconfig'),

    # ex: /videosearch/5
    url(r'^(?P<task_id>[0-9]+)/$', views.detail, name='detail'),

    url(r'^platforms$', views.platforms, name='platforms'),

    #url(r'^platform_config$', views.platform_config, name='platform_config')


    #
    # # ex: /polls/5/results/
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    #
    # # ex: /polls/5/vote/
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]