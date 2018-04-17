from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import logout,login
from cms_users_put import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^login$',login),
    url(r'^logout$',logout),
    url(r'^$','cms_users_put.views.show_content'),
    url(r'^(.*)','cms_users_put.views.cms_users_put'),
    url(r'^admin/', include(admin.site.urls)),
)
