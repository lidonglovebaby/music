from django.conf.urls import patterns, url
from musicworld import views

#set urls to show specific page
urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^article/$', views.article, name='article'),
    url(r'^article/create/$', views.create_article, name='create_article'),
    url(r'^(?P<article_id>\d+)/$', views.detail, name='detail'),
    url(r'^article/(?P<article_id>\d+)/$', views.adetail, name='adetail'),
    url(r'^login/$',views.login,name = 'login'),
    url(r'^user/$',views.user,name = 'user'),
    url(r'^regist/$',views.regist,name = 'regist'),
    url(r'^index/$',views.index,name = 'index'),
    url(r'^logout/$',views.logout,name = 'logout'),
    url(r'^(?P<article_id>\d+)/createcomment/$', views.create, name='create'),
    url(r'^article/like/(?P<article_id>\d+)/$', views.like_article, name='like_article'),
    url(r'^likep/(?P<periodical_id>\d+)/$', views.like_periodical, name='like_periodical'),
    url(r'^periodical/$', views.phome, name='phome'),
    url(r'^periodical/(?P<periodical_id>\d+)/$', views.pdetail, name='pdetail'),
    url(r'^video/$', views.video, name='video'),
    url(r'^contact/$', views.contact, name='contact'),
    
    url(r'^(?P<periodical_id>\d+)/createpcomment/$', views.pcreate, name='pcreate'),
)