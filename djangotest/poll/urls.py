from django.conf.urls import url

from poll import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<q_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<q_id>\d+)/results/$', views.results, name='results'),
    url(r'^(?P<q_id>\d+)/vote/$', views.vote, name='vote'),
]