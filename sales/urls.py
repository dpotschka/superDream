from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ipnListener/$', views.ipnListener, name='ipnListener'),
    url(r'^sendProduct/$', views.sendProduct, name='sendProduct'),
]