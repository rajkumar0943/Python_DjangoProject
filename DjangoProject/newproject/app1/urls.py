from django.conf.urls import include, url

from  app1.views import *

urlpatterns = [
    # Examples:
    # url(r'^$', 'newproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^home/$', home),
    url(r'^departments/(?P<number>[0-9])/$', departmentIdView),
    url(r'^employees/(?P<number>[0-9])/$', employeeIdView),
]
