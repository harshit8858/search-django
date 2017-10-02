
from django.conf.urls import url
from django.contrib import admin
from myapp.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',index),
    url(r'^detail/(\d+)/$',detail,name='detail'),
    url(r'^delete/(\d+)/(\w+)/$',del_record,name='delete'),
    url(r'^edit/(\d+)/(\w+)/$',edit_record),
    url(r'^search_query/$',search),
    url(r'^contact/$',contact),
    url(r'^success/$',success),
    
]
