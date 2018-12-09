#Django native imports
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic import edit

# Import from our apps
from client import views

urlpatterns = [
    url(r'^$', login_required(views.ClientCreate.as_view()), name='client_create'),
    url(r'^edit/(?P<pk>\d+)/$', login_required(views.ClientUpdate.as_view()), name='client_edit'),
    url(r'^list$', login_required(views.ClientList.as_view()), name='client_list'),
    url(r'^delete/(?P<pk>\d+)/$', login_required(views.ClientDelete.as_view()), name='client_delete'),
    url(r'^(?P<pk>\d+)/$', login_required(views.ClientDetail.as_view()), name='client_detail'),
              ]