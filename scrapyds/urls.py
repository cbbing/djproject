from django.conf.urls import url, static

from . import views

urlpatterns = [

    # ex : /videosearch/
    # url(r'^$', views.IndexView.as_view(), name='index'),
    # url(r'^index/$', views.index),
    url(r'^jobs/$', views.jobs),
    # url(r'^success/$', views.success),
    # url(r'^max_date/(.+)/$', views.max_date),

]