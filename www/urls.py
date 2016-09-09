from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^forgot_password/$', views.forgot_password, name='forgot_password'),
    url(r'^loan_app/$', views.loan_app, name='loan_app'),
]
