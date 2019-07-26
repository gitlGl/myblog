from django.contrib import admin
from django.urls import path,re_path
import blog1.views as bv
from django.conf.urls import url
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns

#from django.contrib import staticfiles

app_name = 'blog1'
urlpatterns = [
    url(r'^$', bv.index, name='index'),
    url('index', bv.index, name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', bv.detail, name='detail'),

    url(r'^timelist/$', bv.time_list_conment, name='time_list_conment'),

    #url(r'^Category_page/$', bv.Category_page, name='Category_page'),
    url(r'^Category_page/(?P<category1>[0-9]+)/$', bv.Category_page,
        name='Category_page'),
    url('bowen', bv.bowen, name='bowen'),
    url('trys', bv.trys, name='trys'),

]


#urlpatterns += staticfiles_urlpatterns()