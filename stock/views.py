#Django native imports
from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.urls import reverse_lazy
from django.utils.translation import ugettext as _
from django.views import generic

# Import from our apps
from stock.forms import ClothesForm
from stock.models import Clothes


class ClothesCreate(generic.CreateView):
    model = Clothes
    form_class = ClothesForm   
    template_name = 'stock/clothes_form.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.created_by = self.request.user.username
        obj.save()
        messages.success(self.request, _('Item successfully created'))
        return HttpResponseRedirect('list')


class ClothesUpdate(generic.UpdateView):
    """
    Update view for server edit page. Upon clicking "Edit" button on the
    item view page, user will be able to update a server by utilising
    this view.
    """

    model = Clothes
    form_class = ClothesForm
    template_name_suffix = '_update_form'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        #if not request.user.is_authenticated():
        #    return HttpResponseRedirect(reverse('login', args=(request.user.id,)))
        return super(ClothesUpdate, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        """
        If the form is valid, save the associated model
        """
        obj = form.save(commit=False)
        obj.created_by = self.request.user.username
        obj.save()
        messages.success(self.request, _('Item successfully updated'))
        return render(self.request, 'stock/clothes_update_form.html', {'form': form})


class ClothesList(generic.ListView):
    """
    List view for the items
    """
    model = Clothes
    template_name = 'stock/clothes_list.html'
    paginate_by = 50

    def get_queryset(self):
        qs = Clothes.objects.all()
        return qs.order_by('-code')

class ClothesSoldList(generic.ListView):
    model = Clothes
    template_name = 'stock/clothes_sold_list.html'
    paginate_by = 50

    def get_queryset(self):
        qs = Clothes.objects.filter(sold=True)
        return qs.order_by('code')

class ClothesLoanList(generic.ListView):
    model = Clothes
    template_name = 'stock/clothes_loan_list.html'
    paginate_by = 50

    def get_queryset(self):
        qs = Clothes.objects.filter(debt=True)
        return qs.order_by('code')


class ClothesDetail(generic.DetailView):
    """
    Detail view for a single server. This view is shown on the webpage 
    when user clicks on a single server in "Server list" page
    """

    model = Clothes
    template_name = 'stock/clothes_detail.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(ClothesDetail, self).get(request, *args, **kwargs)


class ClothesDelete(generic.DeleteView):
    model = Clothes
    success_url = reverse_lazy('clothes_list')
