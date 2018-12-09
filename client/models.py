from django.db import models
from django.urls import reverse, reverse_lazy
from django.utils.translation import ugettext as _


# Create your models here.

class Client(models.Model):

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100, default=None)
    
    #Models
    name = models.CharField(_("Имя клиента"), max_length=30)
    phone = models.CharField(_("Телефон"), max_length=30, default=None)
    email = models.EmailField(_("Электронный адрес"), max_length=254, default=None)
    debt = models.DecimalField(_("Долг"), max_digits=5, decimal_places=2)


    def __str__(self):
        return name

    def get_absolute_url(self):
        """
        Handy way of getting the url of the object to its detail view page
        """
        return reverse('client_edit', args=[str(self.pk)])

    def get_detail(self):
        """
        Handy way of getting the url of the object to its detail view page
        """
        return reverse('client_detail', args=[str(self.pk)])

    def get_delete(self):
        """
        Handy way of getting the url of the object to its delete view page
        """
        return reverse('client_delete', args=[str(self.pk)])

    def get_class(self):
        """
        Handy way of getting the class of the object for the html templates
        """
        class_name = "Client"
        return class_name

    class Meta:
        verbose_name_plural = "Clients"
