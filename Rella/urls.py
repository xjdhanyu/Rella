from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'main.views.index', name='index'),
    url(r'^task/list/$', 'main.views.task_list', name='task_list'),
    url(r'^task/(?P<task_id>\d+)/$', 'main.views.task', name='task'),
    url(r'^task/add/$', 'main.views.task_add', name='task_add'),
    url(r'^task/edit/(?P<task_id>\d+)/$', 'main.views.task_edit', name='task_edit'),
    url(r'^task/delete/(?P<task_id>\d+)/$', 'main.views.task_delete', name='task_delete'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
