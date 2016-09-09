from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^loan_app/$', views.loan_app, name='loan_app'),
    #url(r'^login/$', views.login, name='login'),
    #url(r'^home/$', views.home, name='home'),
    #url(r'^logout/$', views.logout, name='logout'),
]
