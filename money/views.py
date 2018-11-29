#Django native imports
from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.urls import reverse_lazy
from django.utils.translation import ugettext as _
from django.views import generic

# Import from our apps
from money.forms import MoneyForm
from money.models import Money


class MoneyCreate(generic.CreateView):
    model = Money
    form_class = MoneyForm   
    template_name = 'money/money_form.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.created_by = self.request.user.username
        obj.save()
        messages.success(self.request, _('Item successfully created'))
        return HttpResponseRedirect('list')

class MoneyList(generic.ListView):
    """
    List view for the items
    """
    model = Money
    template_name = 'money/money_list.html'
    paginate_by = 50

class MoneyDetail(generic.DetailView):
    """
    Detail view for a single server. This view is shown on the webpage 
    when user clicks on a single server in "Server list" page
    """

    model = Money
    template_name = 'money/money_detail.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(MoneyDetail, self).get(request, *args, **kwargs)


class MoneyDelete(generic.DeleteView):
    model = Money
    success_url = reverse_lazy('money_list')

class MoneyUpdate(generic.UpdateView):
    """
    Update view for server edit page. Upon clicking "Edit" button on the
    item view page, user will be able to update a server by utilising
    this view.
    """

    model = Money
    form_class = MoneyForm
    template_name_suffix = '_update_form'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        #if not request.user.is_authenticated():
        #    return HttpResponseRedirect(reverse('login', args=(request.user.id,)))
        return super(MoneyUpdate, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        """
        If the form is valid, save the associated model
        """
        obj = form.save(commit=False)
        obj.created_by = self.request.user.username
        obj.save()
        messages.success(self.request, _('Item successfully updated'))
        return render(self.request, 'money/money_update_form.html', {'form': form})