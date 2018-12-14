#Django native imports
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic import edit

# Import from our apps
from expence import views

urlpatterns = [
    url(r'^$', login_required(views.ExpenceCreate.as_view()), name='expence_create'),
    url(r'^edit/(?P<pk>\d+)/$', login_required(views.ExpenceUpdate.as_view()), name='expence_edit'),
    url(r'^list$', login_required(views.ExpenceList.as_view()), name='expence_list'),
    url(r'^delete/(?P<pk>\d+)/$', login_required(views.ExpenceDelete.as_view()), name='expence_delete'),
    url(r'^(?P<pk>\d+)/$', login_required(views.ExpenceDetail.as_view()), name='expence_detail'),
              ]