from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'mockHN.views.home',name="home"),
    url(r'^page/(?P<num>\d+)^$', 'mockHN.views.page',name="page"),
    url(r'^index/$', 'mockHN.views.home',name="home"),
    url(r'^user/(?P<user_id>[A-Za-z][A-Za-z0-9!@#$%^&_*]*)$', 'mockHN.views.user',name="user"),
    url(r'^comment/(?P<comment_id>\d+)$', 'mockHN.views.comment',name="comment"),
    url(r'^comments/(?P<item_id>\d+)$', 'mockHN.views.comment',name="comments"),
    url(r'^story/(?P<story_id>\d+)$', 'mockHN.views.story',name="story"),
    url(r'^range/$', 'mockHN.views.story_handle',name="story_handle"),
)
