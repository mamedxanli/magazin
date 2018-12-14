#Django native imports
from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.urls import reverse_lazy
from django.utils.translation import ugettext as _
from django.views import generic

# Import from our apps
from expence.forms import ExpenceForm
from expence.models import Expence


class ExpenceCreate(generic.CreateView):
    model = Expence
    form_class = ExpenceForm   
    template_name = 'expence/expence_form.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.created_by = self.request.user.username
        obj.save()
        messages.success(self.request, _('Item successfully created'))
        return HttpResponseRedirect('list')

class ExpenceList(generic.ListView):
    """
    List view for the items
    """
    model = Expence
    template_name = 'expence/expence_list.html'
    paginate_by = 50

class ExpenceDetail(generic.DetailView):
    """
    Detail view for a single server. This view is shown on the webpage 
    when user clicks on a single server in "Server list" page
    """

    model = Expence
    template_name = 'expence/expence_detail.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(ExpenceDetail, self).get(request, *args, **kwargs)


class ExpenceDelete(generic.DeleteView):
    model = Expence
    success_url = reverse_lazy('expence_list')

class ExpenceUpdate(generic.UpdateView):
    """
    Update view for server edit page. Upon clicking "Edit" button on the
    item view page, user will be able to update a server by utilising
    this view.
    """

    model = Expence
    form_class = ExpenceForm
    template_name_suffix = '_update_form'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        #if not request.user.is_authenticated():
        #    return HttpResponseRedirect(reverse('login', args=(request.user.id,)))
        return super(ExpenceUpdate, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        """
        If the form is valid, save the associated model
        """
        obj = form.save(commit=False)
        obj.created_by = self.request.user.username
        obj.save()
        messages.success(self.request, _('Item successfully updated'))
        return render(self.request, 'expence/expence_update_form.html', {'form': form})