#Django native imports
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic import edit

# Import from our apps
from money import views

urlpatterns = [
    url(r'^$', login_required(views.MoneyCreate.as_view()), name='money_create'),
    url(r'^edit/(?P<pk>\d+)/$', login_required(views.MoneyUpdate.as_view()), name='money_edit'),
    url(r'^list$', login_required(views.MoneyList.as_view()), name='money_list'),
    url(r'^delete/(?P<pk>\d+)/$', login_required(views.MoneyDelete.as_view()), name='money_delete'),
    url(r'^(?P<pk>\d+)/$', login_required(views.MoneyDetail.as_view()), name='money_detail'),
              ]