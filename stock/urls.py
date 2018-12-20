#Django native imports
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic import edit

# Import from our apps
from stock import views

urlpatterns = [
    url(r'^$', login_required(views.ClothesCreate.as_view()), name='clothes_create'),
    url(r'^edit/(?P<pk>\d+)/$', login_required(views.ClothesUpdate.as_view()), name='clothes_edit'),
    url(r'^list$', login_required(views.ClothesList.as_view()), name='clothes_list'),
    url(r'^sold_list$', login_required(views.ClothesSoldList.as_view()), name='clothes_sold_list'),
    url(r'^delete/(?P<pk>\d+)/$', login_required(views.ClothesDelete.as_view()), name='clothes_delete'),
    url(r'^(?P<pk>\d+)/$', login_required(views.ClothesDetail.as_view()), name='clothes_detail'),
              ]