#Django native imports
from django.views import generic
from django.shortcuts import render, render_to_response

# Python imports
from itertools import chain

# Import from our apps
from stock.models import Clothes
from money.models import Money
from expence.models import Expence

class HomePage(generic.TemplateView):
    template_name = "inetrecomgr/index.html"
    context_object_name = 'context'

    def get_context_data(self,**kwargs):
        """
        We have a qs per model to be queried, then is merged
        using the chain and returned to the view
        """
        context = super().get_context_data(**kwargs)
        #context['clothes_stock']  = Clothes.objects.filter(sold=False)
        context['clothes_sold']  = Clothes.objects.filter(sold=True)
        context['clothes_stock_amount'] = Clothes.get_amount_in_stock(self)
        context['clothes_stock']  = Clothes.get_number_of_items_in_stock(self)
        context['money_amount'] = Money.get_money_for_month(self)
        context['expence_amount'] = Expence.get_expence_for_month(self)
        return context

"""
General view for all our apps, all reports from the navbar are under
"""

"""
IP Reports below
"""

class IPlist_Used(generic.ListView):
    """
    Queries all the existing objects in the DB for devices,
    Then return them as context for the view
    """
    template_name = "inetrecomgr/IP_used_list.html"
    context_object_name = 'ip_list'
    paginate_by = 25

    def get_context_data(self, **kwargs):
        """
        Feeds more context data to the template, see Stations_Sept_Receivers comments.
        """
        context = super().get_context_data(**kwargs)
        context['page_title'] = "IPs in use"
        context['table_title'] = "Overview of IPs in use"
        return context

    def get_queryset(self):
        """
        We have a qs per model to be queried, then is merged
        using the chain and returned to the view
        """
        qs1 = Netdev.objects.filter(decomissioned=False)
        qs2 = Server.objects.filter(decomissioned=False)
        qs4 = Vserver.objects.filter(decomissioned=False)
        ip_list = list(chain(qs1, qs2, qs4))
        return ip_list


class IPlist_Decomissioned(generic.ListView):
    """
    Queries all the existing objects in the DB for devices,
    Then return them as context for the view
    """
    template_name = "inetrecomgr/IP_decomissioned_list.html"
    context_object_name = 'ip_list'
    paginate_by = 25

    def get_context_data(self, **kwargs):
        """
        Feeds more context data to the template, see Stations_Sept_Receivers comments.
        """
        context = super().get_context_data(**kwargs)
        context['page_title'] = "IPs Decomissioned"
        context['table_title'] = "Overview of decomissioned IPs in our infrastructure"
        return context

    def get_queryset(self):
        """
        We have a qs per model to be queried, then is merged
        using the chain and returned to the view
        """
        qs1 = Netdev.objects.filter(decomissioned=True)
        qs2 = Server.objects.filter(decomissioned=True)
        qs4 = Vserver.objects.filter(decomissioned=True)
        ip_list = list(chain(qs1,qs2,qs4))
        return ip_list


class IPlist_All(generic.ListView):
    """
    Queries all the existing objects in the DB for devices,
    Then return them as context for the view
    """
    template_name = "inetrecomgr/IP_all_list.html"
    context_object_name = 'ip_list'
    paginate_by = 25

    def get_context_data(self, **kwargs):
        """
        Feeds more context data to the template, see Stations_Sept_Receivers comments.
        """
        context = super().get_context_data(**kwargs)
        context['page_title'] = "IPs All"
        context['table_title'] = "Overview of all IPs in our infrastructure"
        return context

    def get_queryset(self):
        """
        We have a qs per model to be queried, then is merged
        using the chain and returned to the view
        """
        qs1 = Netdev.objects.all().order_by("decomissioned")
        qs2 = Server.objects.all().order_by("decomissioned")
        qs4 = Vserver.objects.all().order_by("decomissioned")
        ip_list = list(chain(qs1,qs2,qs4))
        return ip_list


class IPlist_Public(generic.ListView):
    """
    Queries all the existing objects in the DB for devices,
    Then return them as context for the view
    """
    template_name = "inetrecomgr/IP_public_list.html"
    context_object_name = 'ip_list'
    paginate_by = 25

    def get_context_data(self, **kwargs):
        """
        Feeds more context data to the template, see Stations_Sept_Receivers comments.
        """
        context = super().get_context_data(**kwargs)
        context['page_title'] = "IPs Public"
        context['table_title'] = "Overview of used public IPs in our infrastructure"
        return context

    def get_queryset(self):
        """
        We have a qs per model to be queried, then is merged
        using the chain and returned to the view
        """
        qs1 = Netdev.objects.all().order_by("decomissioned")
        qs2 = Server.objects.all().order_by("decomissioned")
        qs4 = Vserver.objects.all().order_by("decomissioned")
        ip_list = list(chain(qs1,qs2,qs4))
        return ip_list


class IPlist_ILO(generic.ListView):
    """
    Queries all the existing objects in the DB for devices,
    Then return them as context for the view
    """
    template_name = "inetrecomgr/IP_ilo_list.html"
    context_object_name = 'ip_list'
    paginate_by = 25

    def get_context_data(self, **kwargs):
        """
        Feeds more context data to the template, see Stations_Sept_Receivers comments.
        """
        context = super().get_context_data(**kwargs)
        context['page_title'] = "IPs iLO"
        context['table_title'] = "Overview of iLO IPs in our infrastructure"
        return context

    def get_queryset(self):
        qs1 = Server.objects.all().order_by("location")
        ip_list = qs1
        return ip_list


class IPlist_Servers(generic.ListView):
    """
    Queries all the existing objects in the DB for devices,
    Then return them as context for the view
    """
    template_name = "inetrecomgr/IP_servers_list.html"
    context_object_name = 'ip_list'
    paginate_by = 25

    def get_context_data(self, **kwargs):
        """
        Feeds more context data to the template, see Stations_Sept_Receivers comments.
        """
        context = super().get_context_data(**kwargs)
        context['page_title'] = "IPs Servers"
        context['table_title'] = "Overview of servers IPs in our infrastructure"
        return context

    def get_queryset(self):
        """
        We have a qs per model to be queried, then is merged
        using the chain and returned to the view
        """
        qs1 = Server.objects.all().order_by("decomissioned")
        qs2 = Vserver.objects.all().order_by("decomissioned")
        ip_list = list(chain(qs1,qs2))
        return ip_list

class IPlist_Netdevs(generic.ListView):
    """
    Queries all the existing objects in the DB for devices,
    Then return them as context for the view
    """
    template_name = "inetrecomgr/IP_netdevs_list.html"
    context_object_name = 'ip_list'
    paginate_by = 25

    def get_context_data(self, **kwargs):
        """
        Feeds more context data to the template, see Stations_Sept_Receivers comments.
        """
        context = super().get_context_data(**kwargs)
        context['page_title'] = "IPs Network Devices"
        context['table_title'] = "Overview of network devices IPs in our infrastructure"
        return context

    def get_queryset(self):
        qs1 = Netdev.objects.all().order_by("decomissioned")
        ip_list = qs1
        return ip_list

"""
End of IP Reports
"""