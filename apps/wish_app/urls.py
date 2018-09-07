from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^add_item$', views.add_item, name='add_item'),
    url(r'^add$', views.add, name='add'),
    url(r'^delete/(?P<wish_pk>\d+)$', views.delete, name='delete'),
    url(r'^remove/(?P<wish_pk>\d+)$', views.remove, name='remove'),
    url(r'^add_to/(?P<wish_pk>\d+)$', views.add_to, name='add_to'),
    url(r'^who_added/(?P<wish_pk>\d+)$', views.who_added, name='who_added'),
    url(r'^logout$', views.logout, name='logout'),
    # url(r'^create$', views.create, name='create'),
]