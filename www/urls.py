from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^contact-form/$', views.contact_form),
    # url(r'^contact/$', views.contact),
    url(r'^print_redirect.html/$', views.print_redirect),
]
